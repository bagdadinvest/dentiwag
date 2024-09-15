# Generated by Django 5.0.9 on 2024-09-13 07:25

import django.db.models.deletion
import modelcluster.fields
import wagtail.contrib.forms.models
import wagtail.fields
import wagtail.models
import wagtail.search.index
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        ('wagtailcore', '0001_initial'),
        ('wagtailimages', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_url', models.URLField(blank=True, verbose_name='Twitter URL')),
                ('github_url', models.URLField(blank=True, verbose_name='GitHub URL')),
                ('organisation_url', models.URLField(blank=True, verbose_name='Organisation URL')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserApprovalTaskState',
            fields=[
                ('taskstate_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.taskstate')),
            ],
            bases=('wagtailcore.taskstate',),
        ),
        migrations.AddField(
            model_name='footertext',
            name='latest_revision',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='latest revision'),
        ),
        migrations.AddField(
            model_name='footertext',
            name='live_revision',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='live revision'),
        ),
        migrations.AddField(
            model_name='footertext',
            name='locale',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.locale', verbose_name='locale'),
        ),
        migrations.CreateModel(
            name='FormPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('to_address', models.CharField(blank=True, help_text='Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.', max_length=255, validators=[wagtail.contrib.forms.models.validate_to_address], verbose_name='to address')),
                ('from_address', models.EmailField(blank=True, max_length=255, verbose_name='from address')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='subject')),
                ('body', wagtail.fields.StreamField([('heading_block', 2), ('paragraph_block', 3), ('image_block', 6), ('block_quote', 9), ('embed_block', 10)], block_lookup={0: ('wagtail.blocks.CharBlock', (), {'form_classname': 'title', 'required': True}), 1: ('wagtail.blocks.ChoiceBlock', [], {'blank': True, 'choices': [('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], 'required': False}), 2: ('wagtail.blocks.StructBlock', [[('heading_text', 0), ('size', 1)]], {}), 3: ('wagtail.blocks.RichTextBlock', (), {'icon': 'pilcrow', 'template': 'blocks/paragraph_block.html'}), 4: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': True}), 5: ('wagtail.blocks.CharBlock', (), {'required': False}), 6: ('wagtail.blocks.StructBlock', [[('image', 4), ('caption', 5), ('attribution', 5)]], {}), 7: ('wagtail.blocks.TextBlock', (), {}), 8: ('wagtail.blocks.CharBlock', (), {'blank': True, 'label': 'e.g. Mary Berry', 'required': False}), 9: ('wagtail.blocks.StructBlock', [[('text', 7), ('attribute_name', 8)]], {}), 10: ('wagtail.embeds.blocks.EmbedBlock', (), {'help_text': 'Insert an embed URL e.g https://www.youtube.com/watch?v=SGJFWirQ3ks', 'icon': 'media', 'template': 'blocks/embed_block.html'})})),
                ('thank_you_text', wagtail.fields.RichTextField(blank=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.forms.models.FormMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.AddField(
            model_name='formfield',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='base.formpage'),
        ),
        migrations.CreateModel(
            name='GalleryPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('introduction', models.TextField(blank=True, help_text='Text to describe the page')),
                ('body', wagtail.fields.StreamField([('heading_block', 2), ('paragraph_block', 3), ('image_block', 6), ('block_quote', 9), ('embed_block', 10)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'form_classname': 'title', 'required': True}), 1: ('wagtail.blocks.ChoiceBlock', [], {'blank': True, 'choices': [('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], 'required': False}), 2: ('wagtail.blocks.StructBlock', [[('heading_text', 0), ('size', 1)]], {}), 3: ('wagtail.blocks.RichTextBlock', (), {'icon': 'pilcrow', 'template': 'blocks/paragraph_block.html'}), 4: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': True}), 5: ('wagtail.blocks.CharBlock', (), {'required': False}), 6: ('wagtail.blocks.StructBlock', [[('image', 4), ('caption', 5), ('attribution', 5)]], {}), 7: ('wagtail.blocks.TextBlock', (), {}), 8: ('wagtail.blocks.CharBlock', (), {'blank': True, 'label': 'e.g. Mary Berry', 'required': False}), 9: ('wagtail.blocks.StructBlock', [[('text', 7), ('attribute_name', 8)]], {}), 10: ('wagtail.embeds.blocks.EmbedBlock', (), {'help_text': 'Insert an embed URL e.g https://www.youtube.com/watch?v=SGJFWirQ3ks', 'icon': 'media', 'template': 'blocks/embed_block.html'})}, verbose_name='Page body')),
                ('collection', models.ForeignKey(blank=True, help_text='Select the image collection for this gallery.', limit_choices_to=models.Q(('name__in', ['Root']), _negated=True), null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.collection')),
                ('image', models.ForeignKey(blank=True, help_text='Landscape mode only; horizontal width between 1000px and 3000px.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('hero_text', models.CharField(help_text='Write an introduction for the bakery', max_length=255)),
                ('hero_cta', models.CharField(help_text='Text to display on Call to Action', max_length=255, verbose_name='Hero CTA')),
                ('body', wagtail.fields.StreamField([('heading_block', 2), ('paragraph_block', 3), ('image_block', 6), ('block_quote', 9), ('embed_block', 10)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'form_classname': 'title', 'required': True}), 1: ('wagtail.blocks.ChoiceBlock', [], {'blank': True, 'choices': [('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], 'required': False}), 2: ('wagtail.blocks.StructBlock', [[('heading_text', 0), ('size', 1)]], {}), 3: ('wagtail.blocks.RichTextBlock', (), {'icon': 'pilcrow', 'template': 'blocks/paragraph_block.html'}), 4: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': True}), 5: ('wagtail.blocks.CharBlock', (), {'required': False}), 6: ('wagtail.blocks.StructBlock', [[('image', 4), ('caption', 5), ('attribution', 5)]], {}), 7: ('wagtail.blocks.TextBlock', (), {}), 8: ('wagtail.blocks.CharBlock', (), {'blank': True, 'label': 'e.g. Mary Berry', 'required': False}), 9: ('wagtail.blocks.StructBlock', [[('text', 7), ('attribute_name', 8)]], {}), 10: ('wagtail.embeds.blocks.EmbedBlock', (), {'help_text': 'Insert an embed URL e.g https://www.youtube.com/watch?v=SGJFWirQ3ks', 'icon': 'media', 'template': 'blocks/embed_block.html'})}, verbose_name='Home content block')),
                ('promo_title', models.CharField(blank=True, help_text='Title to display above the promo copy', max_length=255)),
                ('promo_text', wagtail.fields.RichTextField(blank=True, help_text='Write some promotional copy', max_length=1000, null=True)),
                ('featured_section_1_title', models.CharField(blank=True, help_text='Title to display above the promo copy', max_length=255)),
                ('featured_section_2_title', models.CharField(blank=True, help_text='Title to display above the promo copy', max_length=255)),
                ('featured_section_3_title', models.CharField(blank=True, help_text='Title to display above the promo copy', max_length=255)),
                ('featured_section_1', models.ForeignKey(blank=True, help_text='First featured section for the homepage. Will display up to three child items.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Featured section 1')),
                ('featured_section_2', models.ForeignKey(blank=True, help_text='Second featured section for the homepage. Will display up to three child items.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Featured section 2')),
                ('featured_section_3', models.ForeignKey(blank=True, help_text='Third featured section for the homepage. Will display up to six child items.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Featured section 3')),
                ('hero_cta_link', models.ForeignKey(blank=True, help_text='Choose a page to link to for the Call to Action', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Hero CTA link')),
                ('image', models.ForeignKey(blank=True, help_text='Homepage image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('promo_image', models.ForeignKey(blank=True, help_text='Promo image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('live', models.BooleanField(default=True, editable=False, verbose_name='live')),
                ('has_unpublished_changes', models.BooleanField(default=False, editable=False, verbose_name='has unpublished changes')),
                ('first_published_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='first published at')),
                ('last_published_at', models.DateTimeField(editable=False, null=True, verbose_name='last published at')),
                ('go_live_at', models.DateTimeField(blank=True, null=True, verbose_name='go live date/time')),
                ('expire_at', models.DateTimeField(blank=True, null=True, verbose_name='expiry date/time')),
                ('expired', models.BooleanField(default=False, editable=False, verbose_name='expired')),
                ('locked', models.BooleanField(default=False, editable=False, verbose_name='locked')),
                ('locked_at', models.DateTimeField(editable=False, null=True, verbose_name='locked at')),
                ('first_name', models.CharField(max_length=254, verbose_name='First name')),
                ('last_name', models.CharField(max_length=254, verbose_name='Last name')),
                ('job_title', models.CharField(max_length=254, verbose_name='Job title')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('latest_revision', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='latest revision')),
                ('live_revision', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='live revision')),
                ('locked_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='locked_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='locked by')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
            },
            bases=(wagtail.models.WorkflowMixin, wagtail.models.PreviewableMixin, wagtail.search.index.Indexed, models.Model),
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_suffix', models.CharField(default='The Wagtail Bakery', help_text="The suffix for the title meta tag e.g. ' | The Wagtail Bakery'", max_length=255, verbose_name='Title suffix')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StandardPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('introduction', models.TextField(blank=True, help_text='Text to describe the page')),
                ('body', wagtail.fields.StreamField([('heading_block', 2), ('paragraph_block', 3), ('image_block', 6), ('block_quote', 9), ('embed_block', 10)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'form_classname': 'title', 'required': True}), 1: ('wagtail.blocks.ChoiceBlock', [], {'blank': True, 'choices': [('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], 'required': False}), 2: ('wagtail.blocks.StructBlock', [[('heading_text', 0), ('size', 1)]], {}), 3: ('wagtail.blocks.RichTextBlock', (), {'icon': 'pilcrow', 'template': 'blocks/paragraph_block.html'}), 4: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': True}), 5: ('wagtail.blocks.CharBlock', (), {'required': False}), 6: ('wagtail.blocks.StructBlock', [[('image', 4), ('caption', 5), ('attribution', 5)]], {}), 7: ('wagtail.blocks.TextBlock', (), {}), 8: ('wagtail.blocks.CharBlock', (), {'blank': True, 'label': 'e.g. Mary Berry', 'required': False}), 9: ('wagtail.blocks.StructBlock', [[('text', 7), ('attribute_name', 8)]], {}), 10: ('wagtail.embeds.blocks.EmbedBlock', (), {'help_text': 'Insert an embed URL e.g https://www.youtube.com/watch?v=SGJFWirQ3ks', 'icon': 'media', 'template': 'blocks/embed_block.html'})}, verbose_name='Page body')),
                ('image', models.ForeignKey(blank=True, help_text='Landscape mode only; horizontal width between 1000px and 3000px.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='UserApprovalTask',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.task')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('wagtailcore.task',),
        ),
        migrations.AlterUniqueTogether(
            name='footertext',
            unique_together={('translation_key', 'locale')},
        ),
    ]
