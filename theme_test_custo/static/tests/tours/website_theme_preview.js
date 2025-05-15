import { registry } from "@web/core/registry";

registry.category("web_tour.tours").add("website_theme_preview", {
    url: "/web#action=website.action_website_configuration",
    steps: () => [
{
    content: "Click on create new website",
    trigger: 'button[name="action_website_create_new"]',
    run: "click",
}, {
    content: "insert website name",
    trigger: '[name="name"] input',
    run: "edit Website Test",
}, {
    content: "Validate the website creation modal",
    trigger: ".modal button.btn-primary",
    run: "click",
},
// Configurator first screen
{
    content: "Click Skip and start from scratch",
    trigger: "button:contains('Skip and start from scratch')",
/*
TODO The feature that the following steps are testing is currently disabled.
It will either be restored or entirely removed at some point. See task-3454790.
Also, we simply do not go through theme choice when using "Skip and start from
scratch" in the configurator: the tour flow would have to be adapted.
    run: "click",
}, {
    content: "Click on the Live preview of a theme",
    trigger: ".o_theme_preview button:not(:visible)",
    run: "click",
}, {
    content: "Switch from desktop to mobile preview",
    trigger: ".btn[for=themeViewerMobile]",
    run: "click",
}, {
    content: "Check that the mobile view is active",
    trigger: ".o_view_form_theme_preview_controller .o_field_iframe > div.is_mobile:visible",
    run: () => null, // it's a check
}, {
    content: "Switch back to desktop",
    trigger: ".btn[for=themeViewerDesktop]",
    run: "click",
}, {
    content: "Check that the desktop view is active",
    trigger: ".o_view_form_theme_preview_controller .o_field_iframe > div:not(.is_mobile):visible",
    run: () => null, // it's a check
*/
}]});
