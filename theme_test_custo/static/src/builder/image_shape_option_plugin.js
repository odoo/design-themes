import { Plugin } from "@html_editor/plugin";
import { withSequence } from "@html_editor/utils/resource";
import { registry } from "@web/core/registry";
import { _t } from "@web/core/l10n/translation";

class ThemeTestCustoImageShapeOptionPlugin extends Plugin {
    static id = "themeTestCustoImageShapeOption";
    resources = {
        image_shape_groups_providers: withSequence(10, (shapeGroups) => {
            shapeGroups.basic.subgroups.custom_shape = {
                label: _t("Custom Shapes"),
                shapes: {
                    "theme_test_custo/blob/01": {
                        selectLabel: _t("Blob 01"),
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
    .add(ThemeTestCustoImageShapeOptionPlugin.id, ThemeTestCustoImageShapeOptionPlugin);
