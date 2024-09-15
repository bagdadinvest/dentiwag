# Generated by Django 5.0.9 on 2024-09-13 07:25

import django.db.models.deletion
import modelcluster.fields
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0002_initial'),
        ('wagtailcore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('introduction', models.TextField(blank=True, help_text='Text to describe the page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='RecipePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('date_published', models.DateField(blank=True, null=True, verbose_name='Date article published')),
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('introduction', models.TextField(blank=True, max_length=500)),
                ('backstory', wagtail.fields.StreamField([('heading_block', 2), ('paragraph_block', 3), ('image_block', 6), ('block_quote', 9), ('embed_block', 10)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'form_classname': 'title', 'required': True}), 1: ('wagtail.blocks.ChoiceBlock', [], {'blank': True, 'choices': [('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], 'required': False}), 2: ('wagtail.blocks.StructBlock', [[('heading_text', 0), ('size', 1)]], {}), 3: ('wagtail.blocks.RichTextBlock', (), {'icon': 'pilcrow', 'template': 'blocks/paragraph_block.html'}), 4: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': True}), 5: ('wagtail.blocks.CharBlock', (), {'required': False}), 6: ('wagtail.blocks.StructBlock', [[('image', 4), ('caption', 5), ('attribution', 5)]], {}), 7: ('wagtail.blocks.TextBlock', (), {}), 8: ('wagtail.blocks.CharBlock', (), {'blank': True, 'label': 'e.g. Mary Berry', 'required': False}), 9: ('wagtail.blocks.StructBlock', [[('text', 7), ('attribute_name', 8)]], {}), 10: ('wagtail.embeds.blocks.EmbedBlock', (), {'help_text': 'Insert an embed URL e.g https://www.youtube.com/watch?v=SGJFWirQ3ks', 'icon': 'media', 'template': 'blocks/embed_block.html'})}, help_text='Use only a minimum number of headings and large blocks.')),
                ('recipe_headline', wagtail.fields.RichTextField(blank=True, help_text='Keep to a single line', max_length=120)),
                ('body', wagtail.fields.StreamField([('heading_block', 2), ('paragraph_block', 3), ('block_quote', 6), ('table_block', 7), ('typed_table_block', 12), ('image_block', 15), ('embed_block', 16), ('ingredients_list', 18), ('steps_list', 21)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'form_classname': 'title', 'required': True}), 1: ('wagtail.blocks.ChoiceBlock', [], {'blank': True, 'choices': [('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], 'required': False}), 2: ('wagtail.blocks.StructBlock', [[('heading_text', 0), ('size', 1)]], {'group': 'Content'}), 3: ('wagtail.blocks.RichTextBlock', (), {'group': 'Content', 'icon': 'pilcrow', 'template': 'blocks/paragraph_block.html'}), 4: ('wagtail.blocks.TextBlock', (), {}), 5: ('wagtail.blocks.CharBlock', (), {'blank': True, 'label': 'e.g. Mary Berry', 'required': False}), 6: ('wagtail.blocks.StructBlock', [[('text', 4), ('attribute_name', 5)]], {'group': 'Content'}), 7: ('wagtail.contrib.table_block.blocks.TableBlock', (), {'group': 'Content'}), 8: ('wagtail.blocks.CharBlock', (), {}), 9: ('wagtail.blocks.FloatBlock', (), {}), 10: ('wagtail.blocks.RichTextBlock', (), {}), 11: ('wagtail.images.blocks.ImageChooserBlock', (), {}), 12: ('wagtail.contrib.typed_table_block.blocks.TypedTableBlock', [[('text', 8), ('numeric', 9), ('rich_text', 10), ('image', 11)]], {'group': 'Content'}), 13: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': True}), 14: ('wagtail.blocks.CharBlock', (), {'required': False}), 15: ('wagtail.blocks.StructBlock', [[('image', 13), ('caption', 14), ('attribution', 14)]], {'group': 'Media'}), 16: ('wagtail.embeds.blocks.EmbedBlock', (), {'group': 'Media', 'help_text': 'Insert an embed URL e.g https://www.youtube.com/watch?v=SGJFWirQ3ks', 'icon': 'media', 'template': 'blocks/embed_block.html'}), 17: ('wagtail.blocks.RichTextBlock', (), {'features': ['bold', 'italic', 'link']}), 18: ('wagtail.blocks.ListBlock', (17,), {'group': 'Cooking', 'icon': 'list-ol', 'max_num': 10, 'min_num': 2}), 19: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]}), 20: ('wagtail.blocks.StructBlock', [[('text', 17), ('difficulty', 19)]], {}), 21: ('wagtail.blocks.ListBlock', (20,), {'group': 'Cooking', 'icon': 'tasks', 'max_num': 10, 'min_num': 2})}, help_text='The recipe’s step-by-step instructions and any other relevant information.')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='RecipePersonRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_person_relationship', to='recipes.recipepage')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_recipe_relationship', to='base.person')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
