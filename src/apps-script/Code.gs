/**
 * Beiz enquiry endpoint (Google Apps Script web app).
 * Receives the beiz.com.au contact form, logs it to the "Beiz enquiries" sheet
 * and emails hello@beiz.com.au. No auto-reply to the sender (prevents abuse).
 */
const TO = 'hello@beiz.com.au';
const MAX_PER_HOUR = 30;

function setup() {
  const props = PropertiesService.getScriptProperties();
  let id = props.getProperty('SHEET_ID');
  if (!id) {
    const ss = SpreadsheetApp.create('Beiz enquiries');
    const sh = ss.getSheets()[0];
    sh.setName('Enquiries');
    sh.appendRow(['Received (AEST)', 'Name', 'Email', 'Organisation', 'Area', 'Message', 'Page', 'Status', 'Conflict check (AusTender)', 'Notes']);
    sh.setFrozenRows(1);
    sh.getRange('1:1').setFontWeight('bold');
    id = ss.getId();
    props.setProperty('SHEET_ID', id);
  }
  MailApp.getRemainingDailyQuota();
  return 'Sheet: https://docs.google.com/spreadsheets/d/' + id;
}

function doPost(e) {
  try {
    const body = JSON.parse((e && e.postData && e.postData.contents) || '{}');
    if (body.company_website) return out({ ok: true });               // honeypot
    const clean = (v, n) => String(v || '').replace(/[\u0000-\u001f\u007f]/g, ' ').trim().slice(0, n);
    const d = {
      name: clean(body.name, 120), email: clean(body.email, 160), org: clean(body.organisation, 160),
      topic: clean(body.topic, 80), page: clean(body.page, 200),
      message: String(body.message || '').slice(0, 5000)
    };
    if (!d.name || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(d.email) || !d.message.trim()) return out({ ok: false, error: 'invalid' });

    const cache = CacheService.getScriptCache();
    const n = Number(cache.get('count') || 0);
    if (n >= MAX_PER_HOUR) return out({ ok: false, error: 'busy' });
    cache.put('count', String(n + 1), 3600);

    const id = PropertiesService.getScriptProperties().getProperty('SHEET_ID');
    const when = Utilities.formatDate(new Date(), 'Australia/Sydney', 'yyyy-MM-dd HH:mm');
    const safe = s => /^[=+\-@]/.test(s) ? "'" + s : s;              // stop formula injection
    if (id) SpreadsheetApp.openById(id).getSheetByName('Enquiries')
      .appendRow([when, safe(d.name), safe(d.email), safe(d.org), safe(d.topic), safe(d.message), safe(d.page), 'New', '', '']);

    MailApp.sendEmail({
      to: TO, replyTo: d.email, name: 'Beiz website',
      subject: 'New enquiry: ' + (d.topic || 'General') + ' · ' + d.name,
      body: 'Name: ' + d.name + '\nEmail: ' + d.email + '\nOrganisation: ' + (d.org || '-') + '\nArea: ' + d.topic +
            '\nPage: ' + (d.page || '-') + '\nReceived: ' + when + '\n\n' + d.message +
            '\n\nReminder: run the AusTender conflict check before replying.'
    });
    return out({ ok: true });
  } catch (err) {
    return out({ ok: false, error: 'server' });
  }
}

function doGet() { return out({ ok: true, service: 'beiz-enquiries' }); }
function out(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
