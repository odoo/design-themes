import { Plugin } from "@html_editor/plugin";
import { HeaderTemplateChoice } from "@website/builder/plugins/options/header/header_template_option";
import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";

class ThemeTestCustoHeaderOptionPlugin extends Plugin {
    static id = "themeTestCustoHeaderOption";
    resources = {
        header_templates_providers: [
            () => [
                {
                    key: "custom_theme",
                    Component: HeaderTemplateChoice,
                    props: {
                        id: "header_custom_theme_opt",
                        imgSrc: "/theme_test_custo/static/src/img/template_header_opt.svg",
                        menuShadowClass: "shadow-sm",
                        title: _t("Custom Theme"),
                        varName: "custom-theme",
                        views: ["theme_test_custo.template_header_custom"],
                    },
                },
            ],
        ],
    };
}

registry
    .category("website-plugins")
    .add(ThemeTestCustoHeaderOptionPlugin.id, ThemeTestCustoHeaderOptionPlugin);
