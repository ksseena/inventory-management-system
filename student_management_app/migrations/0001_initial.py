# Generated by Django 3.2.3 on 2021-09-29 06:34

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[(1, 'HOD'), (2, 'Staff'), (4, 'Buyer')], default=1, max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AdminHOD',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StoreItems',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('im_part_no', models.CharField(max_length=100)),
                ('po_number', models.CharField(max_length=100)),
                ('station_name', models.CharField(max_length=100)),
                ('item_name', models.CharField(max_length=100)),
                ('spec', models.CharField(max_length=100)),
                ('product_image', models.ImageField(blank=True, default='product_images/no_attach.png', null=True, upload_to='product_images/%Y/%m/%d/')),
                ('mfr_part_no', models.CharField(max_length=100)),
                ('dummy_part_no', models.CharField(max_length=100)),
                ('mfr', models.CharField(max_length=100)),
                ('current_stock', models.CharField(max_length=100)),
                ('uom', models.CharField(max_length=100)),
                ('unit_price', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=100)),
                ('total_value_wo_gst_usd', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('vendor_name', models.CharField(max_length=100)),
                ('function', models.CharField(max_length=20)),
                ('dri_name', models.CharField(max_length=100)),
                ('life_cycle', models.CharField(max_length=100)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.adminhod')),
            ],
        ),
        migrations.CreateModel(
            name='StoreItems2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('im_part_no', models.CharField(max_length=100)),
                ('po_number', models.CharField(max_length=100)),
                ('station_name', models.CharField(max_length=100)),
                ('item_name', models.CharField(max_length=100)),
                ('spec', models.CharField(max_length=100)),
                ('product_image', models.ImageField(blank=True, default='product_images/no_attach.png', null=True, upload_to='product_images/%Y/%m/%d/')),
                ('mfr_part_no', models.CharField(max_length=100)),
                ('dummy_part_no', models.CharField(max_length=100)),
                ('mfr', models.CharField(max_length=100)),
                ('current_stock', models.CharField(max_length=100)),
                ('uom', models.CharField(max_length=100)),
                ('unit_price', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=100)),
                ('total_value_wo_gst_usd', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('vendor_name', models.CharField(max_length=100)),
                ('function', models.CharField(max_length=20)),
                ('dri_name', models.CharField(max_length=100)),
                ('life_cycle', models.CharField(max_length=100)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.adminhod')),
            ],
        ),
        migrations.CreateModel(
            name='TranferItem2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tranfer_quantity', models.IntegerField()),
                ('tranfer_date', models.CharField(max_length=255)),
                ('item_id1', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.storeitems2')),
                ('item_id2', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.storeitems')),
                ('tranfer_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.adminhod')),
            ],
        ),
        migrations.CreateModel(
            name='TranferItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tranfer_quantity', models.IntegerField()),
                ('tranfer_date', models.CharField(max_length=255)),
                ('item_id1', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.storeitems')),
                ('item_id2', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.storeitems2')),
                ('tranfer_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.adminhod')),
            ],
        ),
        migrations.CreateModel(
            name='ToolUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Staffs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('function', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RequestItem2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=255)),
                ('req_qty', models.IntegerField(default=1)),
                ('line', models.CharField(max_length=50)),
                ('iw_oow', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=100)),
                ('approved_date', models.CharField(max_length=100)),
                ('approved_dri_name', models.CharField(max_length=100)),
                ('machine_sl_no', models.CharField(default='NA', max_length=200)),
                ('machine_name', models.CharField(default='NA', max_length=200)),
                ('station', models.CharField(default='NA', max_length=200)),
                ('remark', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=200)),
                ('issued_status', models.CharField(default='', max_length=100)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.storeitems2')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.staffs')),
            ],
        ),
        migrations.CreateModel(
            name='RequestItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=255)),
                ('req_qty', models.IntegerField(default=1)),
                ('line', models.CharField(max_length=50)),
                ('iw_oow', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=100)),
                ('approved_date', models.CharField(max_length=100)),
                ('approved_dri_name', models.CharField(max_length=100)),
                ('machine_sl_no', models.CharField(default='NA', max_length=200)),
                ('machine_name', models.CharField(default='NA', max_length=200)),
                ('station', models.CharField(default='NA', max_length=200)),
                ('remark', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=200)),
                ('issued_status', models.CharField(default='', max_length=100)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.storeitems')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.staffs')),
            ],
        ),
        migrations.CreateModel(
            name='ReceiveItemp91',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('receive_qty', models.CharField(max_length=255)),
                ('receive_date', models.CharField(max_length=255)),
                ('receive_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.storeitems')),
                ('receiver_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.adminhod')),
            ],
        ),
        migrations.CreateModel(
            name='ReceiveItemP75',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('receive_qty', models.CharField(max_length=255)),
                ('receive_date', models.CharField(max_length=255)),
                ('receive_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.storeitems2')),
                ('receiver_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.adminhod')),
            ],
        ),
        migrations.CreateModel(
            name='IssueItem2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('issuer_name', models.CharField(max_length=255)),
                ('issuer_mi_id', models.CharField(max_length=255)),
                ('issue_qty', models.IntegerField()),
                ('issue_time', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('request_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.requestitem2')),
            ],
        ),
        migrations.CreateModel(
            name='IssueItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('issuer_name', models.CharField(max_length=255)),
                ('issuer_mi_id', models.CharField(max_length=255)),
                ('issue_qty', models.IntegerField()),
                ('issue_time', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('total_cost', models.CharField(max_length=1000)),
                ('request_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.requestitem')),
            ],
        ),
        migrations.CreateModel(
            name='DamagedItemP91',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_dri_MI_ID', models.CharField(max_length=255)),
                ('user_dri_name', models.CharField(max_length=255)),
                ('reason', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('damaged_qty', models.IntegerField()),
                ('issue_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.issueitem')),
            ],
        ),
        migrations.CreateModel(
            name='DamagedItemP75',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_dri_MI_ID', models.CharField(max_length=255)),
                ('user_dri_name', models.CharField(max_length=255)),
                ('reason', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('damaged_qty', models.IntegerField()),
                ('issue_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.issueitem2')),
            ],
        ),
    ]
