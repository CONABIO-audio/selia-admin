from django.contrib import admin


class CollectionTypeAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    search_fields = ('name', )
    list_display = ('id', 'name',)
    list_filter = (
        'name',
        'anyone_can_create',
        'restrict_site_types',
        'restrict_annotation_types',
        'restrict_item_types',
        'restrict_licence_types',
        'restrict_device_types',
        'restrict_event_types',
        'restrict_sampling_event_types',
    )
    list_display = (
        'id',
        'name',
        'anyone_can_create',
        'restrict_site_types',
        'restrict_annotation_types',
        'restrict_item_types',
        'restrict_licence_types',
        'restrict_device_types',
        'restrict_event_types',
        'restrict_sampling_event_types',
    )
    autocomplete_fields = (
        # 'site_types',
        # 'annotation_types',
        # 'licence_types',
        # 'event_types',
        # 'sampling_event_types',
        # 'item_types',
        # 'device_types',
        # 'roles',
        # 'administrators',
    )

    fieldsets = (
        (None, {
            'fields': (
                ('name', 'logo'),
                'description'
            ),
        }),
        ('Metadata', {
            'classes': ('collapse', ),
            'fields': ('metadata_schema', ),
        }),
        ('Admin and Permissions', {
            'classes': ('collapse', ),
            'fields': (('administrators', 'anyone_can_create'),)
        }),
        ('Restrictions', {
            'classes': ('collapse', ),
            'fields': (
                (
                    'restrict_site_types',
                    'restrict_device_types',
                    'restrict_sampling_event_types'
                ),
                ('restrict_item_types', 'restrict_licence_types'),
                ('restrict_event_types', 'restrict_annotation_types'),
            ),
        }),
        ('Allowed Types', {
            'classes': ('collapse', ),
            'fields': (
                ('site_types', 'sampling_event_types'),
                'licence_types',
                ('event_types', 'annotation_types'),
            )
        })
    )


class CollectionAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    search_fields = (
        'id',
        'name',
        'collection_type__name',
        'institution__institution_name',
    )
    list_display = (
        'id',
        'name',
        'collection_type',
        'institution',
    )
    list_filter = (
        'is_open',
        'collection_type',
        'institution',
    )
    autocomplete_fields = (
        'collection_type',
        'users',
        'administrators',
    )

    fieldsets = (
        (None, {
            'fields': (
                ('collection_type', 'name'),
                ('description',),
                ('institution', 'logo'),
            )
        }),
        ('Metadata', {
            'classes': ('collapse', ),
            'fields': ('metadata', )
        }),
        # ('Sites and Devices', {
            # 'classes': ('collapse', ),
            # 'fields': ('sites', 'physical_devices'),
        # }),
        ('Admin', {
            'classes': ('collapse', ),
            'fields': ('administrators', ),
        }),
        ('Access', {
            'classes': ('collapse', ),
            'fields': ('is_open', ),
        })
    )
