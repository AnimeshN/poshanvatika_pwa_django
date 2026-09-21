from django.contrib import admin

from django.utils.html import format_html

# Register your models here.

from .models import PoshanFormInformation, UploadPictureModel, UploadWellPictureModel, CensusTable, AhmedSchoolForm,KoboPoshan

admin.site.register(UploadWellPictureModel)
admin.site.register(PoshanFormInformation)
admin.site.register(CensusTable)
admin.site.register(AhmedSchoolForm)
admin.site.register(KoboPoshan)

@admin.register(UploadPictureModel)
class UploadPictureModelAdmin(admin.ModelAdmin):

    # ---------------------------------------------------------
    # LIST VIEW
    # ---------------------------------------------------------
    list_display = (
        "id",
        "picture_thumbnail",
        "name",
        "organization",
        "state",
        "district",
        "village",
        "pincode",
        "type",
        "submission_date",
    )

    # ---------------------------------------------------------
    # SEARCH
    # ---------------------------------------------------------
    search_fields = (
        "name",
        "organization",
        "state",
        "district",
        "village",
        "pincode",
        "school_name",
        "type",
    )

    # ---------------------------------------------------------
    # FILTERS
    # ---------------------------------------------------------
    list_filter = (
        "state",
        "district",
        "organization",
        "type",
        "self_made",
        "local_ngo",
        "external_support",
        "community_level",
        "govt_support",
        "school_level",
        "anganwadi",
        "self_consumption",
        "selling_surplus",
        "vegetable",
        "backyard_poultry",
        "backyard_fishery",
        "open_cultivation",
        "open_cultivation_multilayer",
        "protectcultivation_shed_net",
        "protectcultivation_shed_polyhouse",
        "well",
        "pond",
        "bore_well",
        "river",
        "irrigation",
        "mid_day_meal",
        "hot_cooked_meal",
        "school_child",
        "submission_date",
    )

    # ---------------------------------------------------------
    # DEFAULT SORTING
    # ---------------------------------------------------------
    ordering = ("-submission_date",)

    # ---------------------------------------------------------
    # DATE HIERARCHY
    # ---------------------------------------------------------
    date_hierarchy = "submission_date"

    # ---------------------------------------------------------
    # READ ONLY
    # ---------------------------------------------------------
    readonly_fields = (
        "submission_date",
        "picture_preview",
    )

    # ---------------------------------------------------------
    # ITEMS PER PAGE
    # ---------------------------------------------------------
    list_per_page = 50

    # ---------------------------------------------------------
    # IMAGE THUMBNAIL IN LIST
    # ---------------------------------------------------------
    @admin.display(description="Picture")
    def picture_thumbnail(self, obj):

        if obj.picture:
            return format_html(
                '<img src="{}" width="80" height="50" '
                'style="object-fit:cover;border-radius:4px;" />',
                obj.picture.url
            )

        return "No Image"

    # ---------------------------------------------------------
    # LARGE IMAGE PREVIEW IN EDIT PAGE
    # ---------------------------------------------------------
    @admin.display(description="Picture Preview")
    def picture_preview(self, obj):

        if obj.picture:
            return format_html(
                '<img src="{}" style="max-width:500px; '
                'max-height:350px; object-fit:contain;" />',
                obj.picture.url
            )

        return "No Image"

    # ---------------------------------------------------------
    # FIELD GROUPS
    # ---------------------------------------------------------
    fieldsets = (

        (
            "Beneficiary & Location",
            {
                "fields": (
                    "name",
                    "organization",
                    "state",
                    "district",
                    "village",
                    "pincode",
                    "lat",
                    "lng",
                    "type",
                )
            },
        ),

        (
            "Picture",
            {
                "fields": (
                    "picture",
                    "picture_preview",
                )
            },
        ),

        (
            "Support & Establishment",
            {
                "fields": (
                    "self_made",
                    "local_ngo",
                    "external_support",
                    "community_level",
                    "govt_support",
                    "school_level",
                    "anganwadi",
                    "others_nutri",
                )
            },
        ),

        (
            "Nutrition & Consumption",
            {
                "fields": (
                    "self_consumption",
                    "selling_surplus",
                    "surplus_addition",
                    "others_level",
                    "vegetable",
                    "backyard_poultry",
                    "backyard_fishery",
                    "others_scale",
                    "surplus",
                    "income",
                )
            },
        ),

        (
            "Vegetables, Fruits & Seeds",
            {
                "fields": (
                    "one_to_fourthousand_sq",
                    "seed_ngo",
                    "seasonal_vegetable",
                    "perennial_vegetable",
                    "fruitsgrown",
                    "dailyfruit",
                    "indigeous",
                )
            },
        ),

        (
            "Cultivation",
            {
                "fields": (
                    "open_cultivation",
                    "open_cultivation_multilayer",
                    "protectcultivation_shed_net",
                    "protectcultivation_shed_polyhouse",
                    "cultivation_others",
                    "month",
                )
            },
        ),

        (
            "Water Sources",
            {
                "fields": (
                    "well",
                    "pond",
                    "canel",
                    "bore_well",
                    "river",
                    "source_water",
                    "irrigation",
                )
            },
        ),

        (
            "School & Community Activities",
            {
                "fields": (
                    "school_name",
                    "any_weekly_class",
                    "weekly",
                    "any_innovative",
                    "mid_day_meal",
                    "surplus_selling",
                    "openfield_science_lab",
                    "hot_cooked_meal",
                    "school_child",
                    "school_scale",
                )
            },
        ),

        (
            "Other",
            {
                "fields": (
                    "nal",
                    "submission_date",
                )
            },
        ),
    )