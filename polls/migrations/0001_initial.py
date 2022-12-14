# Generated by Django 4.0.7 on 2022-08-27 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('accountname', models.CharField(db_column='AccountName', max_length=30, primary_key=True, serialize=False)),
                ('accountname2', models.CharField(db_column='AccountName2', max_length=30)),
                ('locationaddress1', models.CharField(db_column='LocationAddress1', max_length=30)),
                ('locationaddress2', models.CharField(db_column='LocationAddress2', max_length=30)),
                ('locationcity', models.CharField(db_column='LocationCity', max_length=30)),
                ('locationstate', models.CharField(db_column='LocationState', max_length=30)),
                ('locationzip', models.CharField(db_column='LocationZip', max_length=30)),
                ('companycode', models.CharField(db_column='CompanyCode', max_length=30)),
                ('taxidnumber', models.CharField(blank=True, db_column='TaxIDNumber', max_length=30, null=True)),
                ('numberofemployees', models.CharField(blank=True, db_column='NumberOfEmployees', max_length=30, null=True)),
                ('numberofemployessdate', models.DateTimeField(blank=True, db_column='NumberOfEmployessDate', null=True)),
                ('activitystatus', models.CharField(blank=True, db_column='ActivityStatus', max_length=30, null=True)),
                ('activitystatusdate', models.DateTimeField(blank=True, db_column='ActivityStatusDate', null=True)),
                ('groupnumber', models.IntegerField(blank=True, db_column='GroupNumber', null=True)),
                ('accountestablisheddate', models.DateTimeField(blank=True, db_column='AccountEstablishedDate', null=True)),
                ('planyearstartdate', models.DateTimeField(blank=True, db_column='PlanYearStartDate', null=True)),
                ('planyearenddate', models.DateTimeField(blank=True, db_column='PlanYearEndDate', null=True)),
                ('subsequentyearstartdate', models.DateTimeField(blank=True, db_column='SubsequentYearStartDate', null=True)),
                ('industrydescription', models.CharField(blank=True, db_column='IndustryDescription', max_length=30, null=True)),
                ('dualcompanyflag', models.CharField(blank=True, db_column='DualCompanyFlag', max_length=30, null=True)),
                ('complexaccountflag', models.CharField(blank=True, db_column='ComplexAccountFlag', max_length=30, null=True)),
                ('standardindustrycode', models.CharField(blank=True, db_column='StandardIndustryCode', max_length=30, null=True)),
                ('annualizedpremuim', models.IntegerField(blank=True, db_column='AnnualizedPremuim', null=True)),
                ('noouststandinginvoices', models.IntegerField(blank=True, db_column='NoOuststandingInvoices', null=True)),
                ('nomonthsinactive', models.IntegerField(blank=True, db_column='NoMonthsInactive', null=True)),
                ('lastinvoicepaiddate', models.DateTimeField(blank=True, db_column='LastInvoicePaidDate', null=True)),
                ('lastinvoicepaidduedate', models.DateTimeField(blank=True, db_column='LastInvoicePaidDueDate', null=True)),
                ('lastinvoicegendate', models.DateTimeField(blank=True, db_column='LastInvoiceGenDate', null=True)),
                ('nextinvoicegendate', models.DateTimeField(blank=True, db_column='NextInvoiceGenDate', null=True)),
                ('lastservicecalldate', models.DateTimeField(blank=True, db_column='LastServiceCallDate', null=True)),
                ('lastbillcount', models.IntegerField(blank=True, db_column='LastBillCount', null=True)),
                ('disabilityofferingstartdate', models.DateTimeField(blank=True, db_column='DisabilityOfferingStartDate', null=True)),
                ('locationphone', models.CharField(blank=True, db_column='LocationPhone', max_length=30, null=True)),
                ('addressinformationsource', models.CharField(blank=True, db_column='AddressInformationSource', max_length=30, null=True)),
                ('webaddress', models.CharField(blank=True, db_column='WebAddress', max_length=30, null=True)),
                ('specialhandlingcode', models.CharField(blank=True, db_column='SpecialHandlingCode', max_length=30, null=True)),
                ('multilocationaccountflag', models.CharField(blank=True, db_column='MultiLocationAccountFlag', max_length=30, null=True)),
                ('peoflag', models.CharField(blank=True, db_column='PEOFlag', max_length=30, null=True)),
                ('disabilityofferingtaxstatus', models.CharField(blank=True, db_column='DisabilityOfferingTaxStatus', max_length=30, null=True)),
                ('transitoneflag', models.CharField(blank=True, db_column='TransitOneFlag', max_length=30, null=True)),
                ('hsaflag', models.CharField(blank=True, db_column='HSAFlag', max_length=30, null=True)),
                ('hraflag', models.CharField(blank=True, db_column='HRAFlag', max_length=30, null=True)),
                ('dataconfidencelevel', models.CharField(blank=True, db_column='DataConfidenceLevel', max_length=30, null=True)),
                ('totalpolicycount', models.IntegerField(blank=True, db_column='TotalPolicyCount', null=True)),
                ('pendingannualizedpremium', models.IntegerField(blank=True, db_column='PendingAnnualizedPremium', null=True)),
                ('percentbylineofbusiness', models.IntegerField(blank=True, db_column='PercentByLineOfBusiness', null=True)),
                ('scheduledlapsedate', models.DateTimeField(blank=True, db_column='ScheduledLapseDate', null=True)),
                ('penetrationpercentage', models.IntegerField(blank=True, db_column='PenetrationPercentage', null=True)),
                ('nofsaparticipants', models.IntegerField(blank=True, db_column='NoFSAParticipants', null=True)),
            ],
            options={
                'db_table': 'Account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Associate',
            fields=[
                ('assoclastname', models.CharField(db_column='AssocLastName', max_length=30, primary_key=True, serialize=False)),
                ('assocfirstname', models.CharField(db_column='AssocFirstName', max_length=30)),
                ('assocmiddleinitial', models.CharField(db_column='AssocMiddleInitial', max_length=30)),
                ('assocsuffix', models.CharField(db_column='AssocSuffix', max_length=30)),
                ('assocdob', models.DateTimeField(db_column='AssocDOB')),
                ('tenuredate', models.DateTimeField(blank=True, db_column='TenureDate', null=True)),
                ('phonenumber', models.CharField(blank=True, db_column='PhoneNumber', max_length=30, null=True)),
            ],
            options={
                'db_table': 'Associate',
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
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
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
            name='Benefitpremiumpredictionmodel',
            fields=[
                ('dataurl', models.CharField(blank=True, db_column='DataURL', max_length=200, null=True)),
                ('modelscripturl', models.CharField(blank=True, db_column='ModelScriptURL', max_length=200, null=True)),
                ('benefitname', models.CharField(db_column='BenefitName', max_length=30, primary_key=True, serialize=False)),
                ('expectedexpenditure', models.FloatField(blank=True, db_column='ExpectedExpenditure', null=True)),
                ('savedmodelurl', models.CharField(blank=True, db_column='SavedModelURL', max_length=200, null=True)),
            ],
            options={
                'db_table': 'BenefitPremiumPredictionModel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Billingaccount',
            fields=[
                ('bacctname', models.CharField(db_column='BAcctName', max_length=30, primary_key=True, serialize=False)),
                ('bacctname2', models.CharField(db_column='BAcctName2', max_length=30)),
                ('billingaddress1', models.CharField(db_column='BillingAddress1', max_length=30)),
                ('billingaddress2', models.CharField(db_column='BillingAddress2', max_length=30)),
                ('billingcity', models.CharField(db_column='BillingCity', max_length=30)),
                ('billingstate', models.CharField(db_column='BillingState', max_length=30)),
                ('billingzip', models.CharField(db_column='BillingZip', max_length=30)),
                ('groupnumber', models.IntegerField(blank=True, db_column='GroupNumber', null=True)),
                ('taxidnumber', models.CharField(blank=True, db_column='TaxIDNumber', max_length=30, null=True)),
                ('onlinebillingflag', models.CharField(blank=True, db_column='OnlineBillingFlag', max_length=30, null=True)),
                ('activitystatus', models.CharField(blank=True, db_column='ActivityStatus', max_length=30, null=True)),
                ('activitystatusdate', models.DateTimeField(blank=True, db_column='ActivityStatusDate', null=True)),
                ('webaddress', models.CharField(blank=True, db_column='WebAddress', max_length=30, null=True)),
                ('payrollprocessorflag', models.CharField(blank=True, db_column='PayrollProcessorFlag', max_length=30, null=True)),
                ('billingphone', models.CharField(blank=True, db_column='BillingPhone', max_length=30, null=True)),
                ('billingaccttypedate', models.DateTimeField(blank=True, db_column='BillingAcctTypeDate', null=True)),
                ('specialhandlingcode', models.CharField(blank=True, db_column='SpecialHandlingCode', max_length=30, null=True)),
                ('changefilesflag', models.CharField(blank=True, db_column='ChangeFilesFlag', max_length=30, null=True)),
                ('enrollmentfileflag', models.CharField(blank=True, db_column='EnrollmentFileFlag', max_length=30, null=True)),
                ('debitcardflag', models.CharField(blank=True, db_column='DebitCardFlag', max_length=30, null=True)),
                ('billingfileflag', models.CharField(blank=True, db_column='BillingFileFlag', max_length=30, null=True)),
                ('ftpsite', models.CharField(blank=True, db_column='FTPSite', max_length=30, null=True)),
                ('nextvisitdate', models.DateTimeField(blank=True, db_column='NextVisitDate', null=True)),
            ],
            options={
                'db_table': 'BillingAccount',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('claimnumber', models.IntegerField(db_column='ClaimNumber', primary_key=True, serialize=False)),
                ('claimdate', models.DateTimeField(blank=True, db_column='ClaimDate', null=True)),
                ('settlementdate', models.DateTimeField(blank=True, db_column='SettlementDate', null=True)),
                ('wellnesseligibilitydate', models.DateTimeField(blank=True, db_column='WellnessEligibilityDate', null=True)),
                ('claimnote', models.CharField(blank=True, db_column='ClaimNote', max_length=30, null=True)),
            ],
            options={
                'db_table': 'Claim',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('contractnumber', models.CharField(db_column='ContractNumber', max_length=30, primary_key=True, serialize=False)),
                ('activitystatus', models.CharField(blank=True, db_column='ActivityStatus', max_length=30, null=True)),
                ('activitystatusdate', models.DateTimeField(blank=True, db_column='ActivityStatusDate', null=True)),
                ('coveragetype', models.CharField(blank=True, db_column='CoverageType', max_length=30, null=True)),
                ('billingmethod', models.CharField(blank=True, db_column='BillingMethod', max_length=30, null=True)),
                ('individualcompanycode', models.CharField(blank=True, db_column='IndividualCompanyCode', max_length=30, null=True)),
                ('suspendcode', models.CharField(blank=True, db_column='SuspendCode', max_length=30, null=True)),
                ('exceptioncode', models.CharField(blank=True, db_column='ExceptionCode', max_length=30, null=True)),
                ('modalpremium', models.CharField(blank=True, db_column='ModalPremium', max_length=30, null=True)),
                ('autopremiumloan', models.CharField(blank=True, db_column='AutoPremiumLoan', max_length=30, null=True)),
                ('creditcardno', models.CharField(blank=True, db_column='CreditCardNo', max_length=30, null=True)),
                ('expirationdate', models.DateTimeField(blank=True, db_column='ExpirationDate', null=True)),
                ('cardtype', models.CharField(blank=True, db_column='CardType', max_length=30, null=True)),
                ('bankingtransitnumber', models.CharField(blank=True, db_column='BankingTransitNumber', max_length=30, null=True)),
                ('bankingaccounttype', models.CharField(blank=True, db_column='BankingAccountType', max_length=30, null=True)),
                ('bankingaccountnumber', models.CharField(blank=True, db_column='BankingAccountNumber', max_length=30, null=True)),
                ('premiumpaymentlimit', models.CharField(blank=True, db_column='PremiumPaymentLimit', max_length=30, null=True)),
                ('substandardrate', models.CharField(blank=True, db_column='SubstandardRate', max_length=30, null=True)),
                ('valuationinterestcode', models.CharField(blank=True, db_column='ValuationInterestCode', max_length=30, null=True)),
                ('supplementalbenefitplan', models.CharField(blank=True, db_column='SupplementalBenefitPlan', max_length=30, null=True)),
                ('specialassemblycode', models.CharField(blank=True, db_column='SpecialAssemblyCode', max_length=30, null=True)),
                ('inforceflag', models.CharField(blank=True, db_column='InForceFlag', max_length=30, null=True)),
                ('payupdate', models.DateTimeField(blank=True, db_column='PayUpDate', null=True)),
                ('duration', models.CharField(blank=True, db_column='Duration', max_length=30, null=True)),
                ('contractlanguage', models.CharField(blank=True, db_column='ContractLanguage', max_length=30, null=True)),
            ],
            options={
                'db_table': 'Contract',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('custfirstname', models.CharField(db_column='CustFirstName', max_length=30, primary_key=True, serialize=False)),
                ('custmiddleinitial', models.CharField(db_column='CustMiddleInitial', max_length=30)),
                ('custsuffix', models.CharField(db_column='CustSuffix', max_length=30)),
                ('custdob', models.DateTimeField(db_column='CustDOB')),
                ('custsalutation', models.CharField(blank=True, db_column='CustSalutation', max_length=30, null=True)),
                ('custemailaddress', models.CharField(blank=True, db_column='CusteMailAddress', max_length=100, null=True)),
                ('ssn_tin', models.CharField(blank=True, db_column='SSN_TIN', max_length=30, null=True)),
                ('ssn_type', models.CharField(blank=True, db_column='SSN_Type', max_length=30, null=True)),
                ('custlastname', models.CharField(db_column='CustLastName', max_length=30)),
                ('preferredlanguage', models.CharField(blank=True, db_column='PreferredLanguage', max_length=30, null=True)),
                ('startdate', models.DateTimeField(blank=True, db_column='StartDate', null=True)),
                ('enddate', models.DateTimeField(blank=True, db_column='EndDate', null=True)),
                ('bmi', models.FloatField(blank=True, db_column='BMI', null=True)),
                ('numchildren', models.IntegerField(blank=True, db_column='NumChildren', null=True)),
                ('evermarriedflag', models.BooleanField(blank=True, db_column='EverMarriedFlag', null=True)),
                ('sex', models.CharField(blank=True, db_column='Sex', max_length=30, null=True)),
                ('smokerflag', models.BooleanField(blank=True, db_column='SmokerFlag', null=True)),
                ('lastassessmentdate', models.DateTimeField(blank=True, db_column='LastAssessmentDate', null=True)),
            ],
            options={
                'db_table': 'Customer',
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
                ('action_flag', models.SmallIntegerField()),
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
            name='Financialinstitution',
            fields=[
                ('finame', models.CharField(db_column='FIName', max_length=30, primary_key=True, serialize=False)),
                ('fiaddress1', models.CharField(db_column='FIAddress1', max_length=30)),
                ('fiaddress2', models.CharField(db_column='FIAddress2', max_length=30)),
                ('fincity', models.CharField(db_column='FINCity', max_length=30)),
                ('finstate', models.CharField(db_column='FINState', max_length=30)),
                ('finzip', models.CharField(db_column='FINZip', max_length=30)),
                ('fiphone', models.CharField(db_column='FIPhone', max_length=30)),
            ],
            options={
                'db_table': 'FinancialInstitution',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoicenumber', models.IntegerField(db_column='InvoiceNumber', primary_key=True, serialize=False)),
                ('paiddate', models.DateTimeField(blank=True, db_column='PaidDate', null=True)),
                ('duedate', models.DateTimeField(blank=True, db_column='DueDate', null=True)),
                ('rundate', models.DateTimeField(blank=True, db_column='RunDate', null=True)),
            ],
            options={
                'db_table': 'Invoice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Managercontract',
            fields=[
                ('sitcode', models.CharField(db_column='SitCode', max_length=30, primary_key=True, serialize=False)),
                ('companycode', models.CharField(db_column='CompanyCode', max_length=30)),
                ('writingnumber', models.IntegerField(db_column='WritingNumber')),
                ('issuedate', models.DateTimeField(db_column='IssueDate')),
                ('contracttype', models.CharField(blank=True, db_column='ContractType', max_length=30, null=True)),
                ('contractsigndate', models.DateTimeField(blank=True, db_column='ContractSignDate', null=True)),
                ('datetime', models.DateTimeField(blank=True, db_column='Datetime', null=True)),
                ('contractprocessdate', models.DateTimeField(blank=True, db_column='ContractProcessDate', null=True)),
                ('startdate', models.DateTimeField(blank=True, db_column='StartDate', null=True)),
                ('enddate', models.DateTimeField(blank=True, db_column='EndDate', null=True)),
            ],
            options={
                'db_table': 'ManagerContract',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productplan',
            fields=[
                ('lineofbusiness', models.CharField(db_column='LineOfBusiness', max_length=30, primary_key=True, serialize=False)),
                ('seriesname', models.CharField(db_column='SeriesName', max_length=30)),
                ('planname', models.CharField(db_column='PlanName', max_length=30)),
                ('ratebooklocationcode', models.CharField(blank=True, db_column='RatebookLocationCode', max_length=30, null=True)),
                ('plancode', models.CharField(blank=True, db_column='PlanCode', max_length=30, null=True, unique=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=30, null=True)),
            ],
            options={
                'db_table': 'ProductPlan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stateregions',
            fields=[
                ('custstate', models.CharField(db_column='CustState', max_length=30, primary_key=True, serialize=False)),
                ('region', models.CharField(blank=True, db_column='Region', max_length=30, null=True)),
            ],
            options={
                'db_table': 'StateRegions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountAssociate',
            fields=[
                ('sitcode', models.OneToOneField(db_column='SitCode', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='%(class)s_1094', serialize=False, to='polls.managercontract')),
                ('startdate', models.DateTimeField(blank=True, db_column='StartDate', null=True)),
                ('associaterole', models.CharField(blank=True, db_column='AssociateRole', max_length=30, null=True)),
                ('stopdate', models.DateTimeField(blank=True, db_column='StopDate', null=True)),
            ],
            options={
                'db_table': 'Account_Associate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountBillingaccount',
            fields=[
                ('accountname', models.OneToOneField(db_column='AccountName', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='%(class)s_1117', serialize=False, to='polls.account')),
                ('relationshiptype', models.CharField(db_column='RelationshipType', max_length=30)),
                ('startdate', models.DateTimeField(db_column='StartDate')),
                ('billingfrequency', models.CharField(blank=True, db_column='BillingFrequency', max_length=30, null=True)),
                ('nonbillablemonths', models.CharField(blank=True, db_column='NonBillableMonths', max_length=30, null=True)),
                ('enrollmentperiodlength', models.CharField(blank=True, db_column='EnrollmentPeriodLength', max_length=30, null=True)),
                ('fsaclaimsreimbursementmethod', models.CharField(blank=True, db_column='FSAClaimsReimbursementMethod', max_length=30, null=True)),
                ('fsaplantype', models.CharField(blank=True, db_column='FSAPlanType', max_length=30, null=True)),
                ('fsa_urmcap', models.CharField(blank=True, db_column='FSA_URMCap', max_length=30, null=True)),
                ('specificationcode', models.CharField(blank=True, db_column='SpecificationCode', max_length=30, null=True)),
                ('accounttype', models.CharField(blank=True, db_column='AccountType', max_length=30, null=True)),
                ('rcodeaccountflag', models.CharField(blank=True, db_column='RCodeAccountFlag', max_length=30, null=True)),
                ('rcodeassocflag', models.CharField(blank=True, db_column='RCodeAssocFlag', max_length=30, null=True)),
                ('rcodecustomerflag', models.CharField(blank=True, db_column='RCodeCustomerFlag', max_length=30, null=True)),
                ('paymentcardflag', models.CharField(blank=True, db_column='PaymentCardFlag', max_length=30, null=True)),
                ('departmentcode', models.CharField(blank=True, db_column='DepartmentCode', max_length=30, null=True)),
                ('ficaexemptionflag', models.CharField(blank=True, db_column='FICAExemptionFlag', max_length=30, null=True)),
                ('railroadtaxexemptionflag', models.CharField(blank=True, db_column='RailroadTaxExemptionFlag', max_length=30, null=True)),
                ('contributionpercentage', models.CharField(blank=True, db_column='ContributionPercentage', max_length=30, null=True)),
                ('highdeductiblemedicalpaymentplanflag', models.CharField(blank=True, db_column='HighDeductibleMedicalPaymentPlanFlag', max_length=30, null=True)),
                ('medicalhealthinsuranceflag', models.CharField(blank=True, db_column='MedicalHealthInsuranceFlag', max_length=30, null=True)),
                ('singlepointbillingflag', models.CharField(blank=True, db_column='SinglePointBillingFlag', max_length=30, null=True)),
                ('expressreconciliationflag', models.CharField(blank=True, db_column='ExpressReconciliationFlag', max_length=30, null=True)),
                ('fsaservicefee', models.CharField(blank=True, db_column='FSAServiceFee', max_length=30, null=True)),
                ('graceperiodlength', models.CharField(blank=True, db_column='GracePeriodLength', max_length=30, null=True)),
            ],
            options={
                'db_table': 'Account_BillingAccount',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Accountmember',
            fields=[
                ('custlastname', models.OneToOneField(db_column='CustLastName', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='%(class)s_1069', serialize=False, to='polls.customer')),
                ('startdate', models.DateTimeField(db_column='StartDate')),
                ('fsacontributionamount', models.IntegerField(blank=True, db_column='FSAContributionAmount', null=True)),
                ('custbacctdepartmentname', models.CharField(blank=True, db_column='CustBAcctDepartmentName', max_length=30, null=True)),
                ('enddate', models.DateTimeField(blank=True, db_column='EndDate', null=True)),
            ],
            options={
                'db_table': 'AccountMember',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountProductplan',
            fields=[
                ('accountname', models.OneToOneField(db_column='AccountName', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='%(class)s_1164', serialize=False, to='polls.account')),
                ('startdate', models.DateTimeField(db_column='StartDate')),
                ('enddate', models.DateTimeField(blank=True, db_column='EndDate', null=True)),
            ],
            options={
                'db_table': 'Account_ProductPlan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Claimevent',
            fields=[
                ('claimnumber', models.OneToOneField(db_column='ClaimNumber', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='%(class)s_1272', serialize=False, to='polls.claim')),
            ],
            options={
                'db_table': 'ClaimEvent',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Claimimage',
            fields=[
                ('claimnumber', models.OneToOneField(db_column='ClaimNumber', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='%(class)s_1290', serialize=False, to='polls.claim')),
                ('documentid', models.IntegerField(db_column='DocumentId')),
                ('documentclass', models.CharField(blank=True, db_column='DocumentClass', max_length=30, null=True)),
                ('imagetype', models.CharField(blank=True, db_column='ImageType', max_length=30, null=True)),
                ('datereceived', models.DateTimeField(blank=True, db_column='DateReceived', null=True)),
                ('processeddate', models.DateTimeField(blank=True, db_column='ProcessedDate', null=True)),
            ],
            options={
                'db_table': 'ClaimImage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contractbenefit',
            fields=[
                ('contractnumber', models.OneToOneField(db_column='ContractNumber', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='%(class)s_1357', serialize=False, to='polls.contract')),
                ('policycountcontribution', models.CharField(blank=True, db_column='PolicyCountContribution', max_length=30, null=True)),
            ],
            options={
                'db_table': 'ContractBenefit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contractingparty',
            fields=[
                ('contractnumber', models.OneToOneField(db_column='ContractNumber', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='%(class)s_1388', serialize=False, to='polls.contract')),
            ],
            options={
                'db_table': 'ContractingParty',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Criticalinsurancedata',
            fields=[
                ('custfirstname', models.OneToOneField(db_column='CustFirstName', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='%(class)s_1405', serialize=False, to='polls.customer')),
                ('assessmentdate', models.DateTimeField(db_column='AssessmentDate')),
                ('lastassessmentflag', models.BooleanField(blank=True, db_column='LastAssessmentFlag', null=True)),
                ('hypertensionflag', models.BooleanField(blank=True, db_column='HypertensionFlag', null=True)),
                ('prevheartdiseaseflag', models.BooleanField(blank=True, db_column='PrevHeartDiseaseFlag', null=True)),
                ('worktype', models.CharField(blank=True, db_column='WorkType', max_length=30, null=True)),
                ('urbanresidenceflag', models.BooleanField(blank=True, db_column='UrbanResidenceFlag', null=True)),
                ('avgglucoselevel', models.FloatField(blank=True, db_column='AvgGlucoseLevel', null=True)),
                ('prevstrokeflag', models.BooleanField(blank=True, db_column='PrevStrokeFlag', null=True)),
                ('alcoholflag', models.BooleanField(blank=True, db_column='AlcoholFlag', null=True)),
                ('physicalhealthscore', models.IntegerField(blank=True, db_column='PhysicalHealthScore', null=True)),
                ('mentalhealthscore', models.IntegerField(blank=True, db_column='MentalHealthScore', null=True)),
                ('diffwalkingflag', models.BooleanField(blank=True, db_column='DiffWalkingFlag', null=True)),
                ('diabeticflag', models.BooleanField(blank=True, db_column='DiabeticFlag', null=True)),
                ('physicalactivityflag', models.BooleanField(blank=True, db_column='PhysicalActivityFlag', null=True)),
                ('sleeptime', models.IntegerField(blank=True, db_column='SleepTime', null=True)),
                ('asthmaflag', models.BooleanField(blank=True, db_column='AsthmaFlag', null=True)),
                ('kidneydiseaseflag', models.BooleanField(blank=True, db_column='KidneyDiseaseFlag', null=True)),
                ('skincancerflag', models.BooleanField(blank=True, db_column='SkinCancerFlag', null=True)),
            ],
            options={
                'db_table': 'CriticalInsuranceData',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customeraddress',
            fields=[
                ('custlastname', models.OneToOneField(db_column='CustLastName', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='%(class)s_1462', serialize=False, to='polls.customer')),
                ('custaddress2', models.CharField(db_column='CustAddress2', max_length=30)),
                ('custaddress1', models.CharField(db_column='CustAddress1', max_length=30)),
                ('custcity', models.CharField(db_column='CustCity', max_length=30)),
                ('custzip', models.CharField(db_column='CustZip', max_length=30)),
                ('annualstartdate', models.DateTimeField(db_column='AnnualStartDate')),
                ('annualenddate', models.DateTimeField(blank=True, db_column='AnnualEndDate', null=True)),
            ],
            options={
                'db_table': 'CustomerAddress',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Remittance',
            fields=[
                ('finame', models.OneToOneField(db_column='FIName', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='%(class)s_1588', serialize=False, to='polls.financialinstitution')),
                ('remittancefreq', models.CharField(blank=True, db_column='RemittanceFreq', max_length=30, null=True)),
                ('remittancedate', models.DateTimeField(blank=True, db_column='RemittanceDate', null=True)),
                ('paymentmethod', models.CharField(blank=True, db_column='PaymentMethod', max_length=30, null=True)),
                ('paymentdate', models.DateTimeField(blank=True, db_column='PaymentDate', null=True)),
            ],
            options={
                'db_table': 'Remittance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contractpremium',
            fields=[
                ('contractnumber', models.OneToOneField(db_column='ContractNumber', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='%(class)s_1371', serialize=False, to='polls.contractbenefit')),
                ('premiumcode', models.CharField(db_column='PremiumCode', max_length=30)),
                ('annualizedpremium', models.IntegerField(blank=True, db_column='AnnualizedPremium', null=True)),
                ('processdate', models.DateTimeField(blank=True, db_column='ProcessDate', null=True)),
                ('appsigndate', models.DateTimeField(blank=True, db_column='AppSignDate', null=True)),
            ],
            options={
                'db_table': 'ContractPremium',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PremiumMgmtcontract',
            fields=[
                ('contractnumber', models.OneToOneField(db_column='ContractNumber', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='%(class)s_1553', serialize=False, to='polls.contractpremium')),
                ('amount', models.IntegerField(blank=True, db_column='Amount', null=True)),
                ('commissionrate', models.CharField(blank=True, db_column='CommissionRate', max_length=30, null=True)),
            ],
            options={
                'db_table': 'Premium_MgmtContract',
                'managed': False,
            },
        ),
    ]
