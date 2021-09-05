# Generated by Django 3.2.5 on 2021-09-05 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_rbac', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='地区')),
            ],
            options={
                'verbose_name': '地区',
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_title', models.CharField(max_length=32, verbose_name='分公司名称')),
                ('semester', models.IntegerField(default=1, verbose_name='期数')),
                ('price', models.IntegerField(default=1000000, verbose_name='项目款')),
                ('start_date', models.DateField(verbose_name='开始日期')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='结束日期')),
                ('memo', models.CharField(blank=True, max_length=256, null=True, verbose_name='项目说明')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.city', verbose_name='地区')),
            ],
            options={
                'verbose_name': '分公司',
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('tel', models.CharField(help_text='QQ号/微信/手机号', max_length=64, unique=True, verbose_name='联系方式')),
                ('status', models.IntegerField(choices=[(1, '已确认'), (2, '未确认')], default=2, verbose_name='状态')),
                ('gender', models.SmallIntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别')),
                ('source', models.SmallIntegerField(choices=[(1, 'qq群'), (2, '内部转介绍'), (3, '官方网站'), (4, '百度推广'), (5, '360推广'), (6, '搜狗推广'), (7, '腾讯课堂'), (8, '广点通'), (9, '高校宣讲'), (10, '渠道代理'), (11, '51cto'), (12, '智汇推'), (13, '网盟'), (14, 'DSP'), (15, 'SEO'), (16, '裙带'), (17, '其它')], default=1, verbose_name='客户来源')),
                ('education', models.IntegerField(blank=True, choices=[(1, '重点大学'), (2, '普通本科'), (3, '独立院校'), (4, '民办本科'), (5, '大专'), (6, '民办专科'), (7, '高中'), (8, '其他')], null=True, verbose_name='学历')),
                ('graduation_school', models.CharField(blank=True, max_length=64, null=True, verbose_name='毕业学校')),
                ('major', models.CharField(blank=True, max_length=64, null=True, verbose_name='所学专业')),
                ('experience', models.IntegerField(blank=True, choices=[(1, '在校生'), (2, '应届毕业'), (3, '半年以内'), (4, '半年至一年'), (5, '一年至三年'), (6, '三年至五年'), (7, '五年以上')], null=True, verbose_name='工作经验')),
                ('work_status', models.IntegerField(blank=True, choices=[(1, '在职'), (2, '无业')], default=1, null=True, verbose_name='职业状态')),
                ('company', models.CharField(blank=True, max_length=64, null=True, verbose_name='目前就职公司')),
                ('salary', models.CharField(blank=True, max_length=64, null=True, verbose_name='当前薪资')),
                ('date', models.DateField(auto_now_add=True, verbose_name='咨询日期')),
                ('last_consult_date', models.DateField(auto_now_add=True, verbose_name='最后跟进日期')),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='部门')),
            ],
            options={
                'verbose_name': '部门',
                'db_table': 'depart',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='项目')),
            ],
            options={
                'verbose_name': '项目',
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('email', models.CharField(max_length=64, verbose_name='邮箱')),
                ('name', models.CharField(max_length=64, verbose_name='真实姓名')),
                ('gender', models.IntegerField(choices=[(1, '男'), (2, '女')], default=1, verbose_name='性别')),
                ('phone', models.CharField(max_length=32, verbose_name='电话')),
                ('entry_date', models.DateField(auto_now_add=True, verbose_name='入职日期')),
                ('resignation_date', models.DateField(blank=True, null=True, verbose_name='离职日期')),
                ('salary', models.IntegerField(blank=True, null=True, verbose_name='薪资')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.company', verbose_name='所属分公司')),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.department', verbose_name='所属部门')),
                ('roles', models.ManyToManyField(blank=True, to='app_rbac.Role', verbose_name='所有角色')),
            ],
            options={
                'verbose_name': '员工',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='StaffRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('should', models.IntegerField(default=10000, verbose_name='应发')),
                ('later', models.IntegerField(default=0, verbose_name='迟到')),
                ('leave', models.IntegerField(default=0, verbose_name='早退')),
                ('ask_leave', models.IntegerField(default=0, verbose_name='请假')),
                ('fine', models.IntegerField(default=0, verbose_name='罚款')),
                ('actual', models.IntegerField(default=10000, verbose_name='实发')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.userinfo', verbose_name='员工姓名')),
            ],
            options={
                'db_table': 'staff_record',
            },
        ),
        migrations.CreateModel(
            name='PaymentRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, '未审核'), (2, '已审核')], default=1, verbose_name='审核状态')),
                ('pay_type', models.IntegerField(choices=[(1, '项目启动款'), (2, '项目进度款'), (3, '项目尾款'), (4, '项目违约金')], default=1, verbose_name='费用类型')),
                ('paid_fee', models.IntegerField(default=0, verbose_name='金额')),
                ('confirm_date', models.DateTimeField(blank=True, null=True, verbose_name='确认日期')),
                ('note', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('apply_date', models.DateTimeField(auto_now_add=True, verbose_name='申请日期')),
                ('city_list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.city', verbose_name='分公司')),
                ('confirm_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='confirms', to='crm.userinfo', verbose_name='确认人')),
                ('consultant', models.ForeignKey(help_text='最终签单人', on_delete=django.db.models.deletion.CASCADE, to='crm.userinfo', verbose_name='销售顾问')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.customer', verbose_name='客户')),
            ],
            options={
                'db_table': 'payment_record',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='consultant',
            field=models.ForeignKey(blank=True, limit_choices_to={'depart__title': '销售部'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consultant', to='crm.userinfo', verbose_name='项目顾问'),
        ),
        migrations.AddField(
            model_name='customer',
            name='course',
            field=models.ManyToManyField(to='crm.Project', verbose_name='咨询项目'),
        ),
        migrations.AddField(
            model_name='customer',
            name='referral_from',
            field=models.ForeignKey(blank=True, help_text='若此客户是转介绍自内部人员,请在此处选择内部人员姓名', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='internal_referral', to='crm.customer', verbose_name='转介绍自客户'),
        ),
        migrations.CreateModel(
            name='ConsultRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='跟进日期')),
                ('note', models.TextField(verbose_name='内容/说明')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.userinfo', verbose_name='跟踪人')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.customer', verbose_name='所咨询客户')),
            ],
            options={
                'db_table': 'consultrecord',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='manger',
            field=models.ForeignKey(limit_choices_to={'depart__title': '项目部'}, on_delete=django.db.models.deletion.CASCADE, related_name='manager', to='crm.userinfo', verbose_name='项目经理'),
        ),
        migrations.AddField(
            model_name='company',
            name='principal',
            field=models.ManyToManyField(limit_choices_to={'depart__title': '项目部'}, related_name='principal', to='crm.UserInfo', verbose_name='负责人'),
        ),
        migrations.AddField(
            model_name='company',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.project', verbose_name='项目'),
        ),
        migrations.CreateModel(
            name='ChangeCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memo', models.TextField(verbose_name='原因')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_name', to='crm.userinfo', verbose_name='员工姓名')),
                ('origin_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='original_company', to='crm.company', verbose_name='原分公司')),
                ('target_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_company', to='crm.company', verbose_name='目标分公司')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='make_name', to='crm.userinfo', verbose_name='处理人')),
            ],
            options={
                'db_table': 'change_cities',
            },
        ),
    ]
