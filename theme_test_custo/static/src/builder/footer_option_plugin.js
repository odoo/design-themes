import { Plugin } from "@html_editor/plugin";
import { FooterTemplateChoice } from "@website/builder/plugins/options/footer_template_option";
import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";

class ThemeTestCustoFooterOptionPlugin extends Plugin {
    static id = "themeTestCustoFooterOption";
    resources = {
        footer_templates_providers: [
            () => [
                {
                    key: "custom_theme",
                    Component: FooterTemplateChoice,
                    props: {
                        imgSrc: "/theme_test_custo/static/src/img/template_footer_opt.svg",
                        varName: "custom-theme",
                        view: "theme_test_custo.template_footer_custom",
                        title: _t("Custom Theme"),
                    },
                },
            ],
        ],
    };
}

registry
    .category("website-plugins")
    .add(ThemeTestCustoFooterOptionPlugin.id, ThemeTestCustoFooterOptionPlugin);
