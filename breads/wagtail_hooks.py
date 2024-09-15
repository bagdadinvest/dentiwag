from wagtail.admin.filters import WagtailFilterSet
from wagtail.admin.panels import FieldPanel
from wagtail.admin.viewsets.model import ModelViewSet
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup

from bakerydemo.base.filters import RevisionFilterSetMixin
from bakerydemo.breads.models import ImplantMaterial, ImplantType, Country


class ImplantMaterialFilterSet(RevisionFilterSetMixin, WagtailFilterSet):
    class Meta:
        model = ImplantMaterial
        fields = {
            "live": ["exact"],
        }


class ImplantMaterialSnippetViewSet(SnippetViewSet):
    model = ImplantMaterial
    ordering = ("name",)
    search_fields = ("name",)
    filterset_class = ImplantMaterialFilterSet
    inspect_view_enabled = True


class ImplantTypeFilterSet(RevisionFilterSetMixin, WagtailFilterSet):
    class Meta:
        model = ImplantType
        fields = []


class ImplantTypeSnippetViewSet(SnippetViewSet):
    model = ImplantType
    ordering = ("title",)
    search_fields = ("title",)
    filterset_class = ImplantTypeFilterSet


class CountryModelViewSet(ModelViewSet):
    model = Country
    ordering = ("title",)
    search_fields = ("title",)
    icon = "globe"
    inspect_view_enabled = True

    panels = [
        FieldPanel("title"),
    ]


# Grouping snippets under one menu in the Wagtail admin
class ImplantMenuGroup(SnippetViewSetGroup):
    menu_label = "Implant Categories"
    menu_icon = "suitcase"  # You can keep or change the icon
    menu_order = 200  # Menu order (e.g., third place in menu)
    items = (
        ImplantMaterialSnippetViewSet,
        ImplantTypeSnippetViewSet,
        CountryModelViewSet,
    )


register_snippet(ImplantMenuGroup)
