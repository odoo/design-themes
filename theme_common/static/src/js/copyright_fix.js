/**
 * This fix corrects a bug introduced in saas-6 which places the copyright div at
 * the wrong position if website is installed without anything else (website_sale,
 * website_event, website_forum, ...).
 */
odoo.define('theme_common.copyright_fix', function (require) {
    $(document).ready(correctCopyright);

    function correctCopyright() {
        $('#footer').children('.container.mt16.mb8').appendTo($('footer'));
    }
});
