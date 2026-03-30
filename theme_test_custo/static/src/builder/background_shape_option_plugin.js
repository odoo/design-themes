import { Plugin } from "@html_editor/plugin";
import { withSequence } from "@html_editor/utils/resource";
import { registry } from "@web/core/registry";
import { _t } from "@web/core/l10n/translation";

class ThemeTestCustoBackgroundShapeOptionPlugin extends Plugin {
    static id = "themeTestCustoBackgroundShapeOption";
    resources = {
        background_shape_groups_providers: withSequence(10, (shapeGroups) => {
            shapeGroups.basic.subgroups.custom_shape = {
                label: _t("Custom Shapes"),
                shapes: {
                    "theme_test_custo/curves/01": {
                        selectLabel: _t("Curve 01"),
                        transform: false,
                        togglableRatio: true,
                    },
                },
            };
        }),
    };
}

registry
    .category("builder-plugins")
    .add(ThemeTestCustoBackgroundShapeOptionPlugin.id, ThemeTestCustoBackgroundShapeOptionPlugin);
