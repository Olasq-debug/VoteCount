# Generated by Django 4.1.3 on 2022-12-04 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agentname',
            fields=[
                ('name_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(max_length=13)),
                ('pollingunit_uniqueid', models.IntegerField()),
            ],
            options={
                'db_table': 'agentname',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AnnouncedLgaResults',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('lga_name', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'announced_lga_results',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AnnouncedPuResults',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('polling_unit_uniqueid', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'announced_pu_results',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AnnouncedStateResults',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'announced_state_results',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AnnouncedWardResults',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('ward_name', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'announced_ward_results',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lga',
            fields=[
                ('uniqueid', models.AutoField(primary_key=True, serialize=False)),
                ('lga_id', models.IntegerField()),
                ('lga_name', models.CharField(max_length=50)),
                ('state_id', models.IntegerField()),
                ('lga_description', models.TextField(blank=True, null=True)),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'lga',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partyid', models.CharField(max_length=11)),
                ('partyname', models.CharField(max_length=11)),
            ],
            options={
                'db_table': 'party',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PollingUnit',
            fields=[
                ('uniqueid', models.AutoField(primary_key=True, serialize=False)),
                ('polling_unit_id', models.IntegerField()),
                ('ward_id', models.IntegerField()),
                ('lga_id', models.IntegerField()),
                ('uniquewardid', models.IntegerField(blank=True, null=True)),
                ('polling_unit_number', models.CharField(blank=True, max_length=50, null=True)),
                ('polling_unit_name', models.CharField(blank=True, max_length=50, null=True)),
                ('polling_unit_description', models.TextField(blank=True, null=True)),
                ('lat', models.CharField(blank=True, max_length=255, null=True)),
                ('long', models.CharField(blank=True, max_length=255, null=True)),
                ('entered_by_user', models.CharField(blank=True, max_length=50, null=True)),
                ('date_entered', models.DateTimeField(blank=True, null=True)),
                ('user_ip_address', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'polling_unit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('state_id', models.IntegerField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'states',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('uniqueid', models.AutoField(primary_key=True, serialize=False)),
                ('ward_id', models.IntegerField()),
                ('ward_name', models.CharField(max_length=50)),
                ('lga_id', models.IntegerField()),
                ('ward_description', models.TextField(blank=True, null=True)),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'ward',
                'managed': False,
            },
        ),
    ]
