# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    accountname = models.CharField(db_column='AccountName', primary_key=True, max_length=30)  # Field name made lowercase.
    accountname2 = models.CharField(db_column='AccountName2', max_length=30)  # Field name made lowercase.
    locationaddress1 = models.CharField(db_column='LocationAddress1', max_length=30)  # Field name made lowercase.
    locationaddress2 = models.CharField(db_column='LocationAddress2', max_length=30)  # Field name made lowercase.
    locationcity = models.CharField(db_column='LocationCity', max_length=30)  # Field name made lowercase.
    locationstate = models.CharField(db_column='LocationState', max_length=30)  # Field name made lowercase.
    locationzip = models.CharField(db_column='LocationZip', max_length=30)  # Field name made lowercase.
    companycode = models.CharField(db_column='CompanyCode', max_length=30)  # Field name made lowercase.
    taxidnumber = models.CharField(db_column='TaxIDNumber', max_length=30, blank=True, null=True)  # Field name made lowercase.
    numberofemployees = models.CharField(db_column='NumberOfEmployees', max_length=30, blank=True, null=True)  # Field name made lowercase.
    numberofemployessdate = models.DateTimeField(db_column='NumberOfEmployessDate', blank=True, null=True)  # Field name made lowercase.
    activitystatus = models.CharField(db_column='ActivityStatus', max_length=30, blank=True, null=True)  # Field name made lowercase.
    activitystatusdate = models.DateTimeField(db_column='ActivityStatusDate', blank=True, null=True)  # Field name made lowercase.
    groupnumber = models.IntegerField(db_column='GroupNumber', blank=True, null=True)  # Field name made lowercase.
    accountestablisheddate = models.DateTimeField(db_column='AccountEstablishedDate', blank=True, null=True)  # Field name made lowercase.
    planyearstartdate = models.DateTimeField(db_column='PlanYearStartDate', blank=True, null=True)  # Field name made lowercase.
    planyearenddate = models.DateTimeField(db_column='PlanYearEndDate', blank=True, null=True)  # Field name made lowercase.
    subsequentyearstartdate = models.DateTimeField(db_column='SubsequentYearStartDate', blank=True, null=True)  # Field name made lowercase.
    industrydescription = models.CharField(db_column='IndustryDescription', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dualcompanyflag = models.CharField(db_column='DualCompanyFlag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    complexaccountflag = models.CharField(db_column='ComplexAccountFlag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    standardindustrycode = models.CharField(db_column='StandardIndustryCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    annualizedpremuim = models.IntegerField(db_column='AnnualizedPremuim', blank=True, null=True)  # Field name made lowercase.
    noouststandinginvoices = models.IntegerField(db_column='NoOuststandingInvoices', blank=True, null=True)  # Field name made lowercase.
    nomonthsinactive = models.IntegerField(db_column='NoMonthsInactive', blank=True, null=True)  # Field name made lowercase.
    lastinvoicepaiddate = models.DateTimeField(db_column='LastInvoicePaidDate', blank=True, null=True)  # Field name made lowercase.
    lastinvoicepaidduedate = models.DateTimeField(db_column='LastInvoicePaidDueDate', blank=True, null=True)  # Field name made lowercase.
    lastinvoicegendate = models.DateTimeField(db_column='LastInvoiceGenDate', blank=True, null=True)  # Field name made lowercase.
    nextinvoicegendate = models.DateTimeField(db_column='NextInvoiceGenDate', blank=True, null=True)  # Field name made lowercase.
    lastservicecalldate = models.DateTimeField(db_column='LastServiceCallDate', blank=True, null=True)  # Field name made lowercase.
    lastbillcount = models.IntegerField(db_column='LastBillCount', blank=True, null=True)  # Field name made lowercase.
    disabilityofferingstartdate = models.DateTimeField(db_column='DisabilityOfferingStartDate', blank=True, null=True)  # Field name made lowercase.
    locationphone = models.CharField(db_column='LocationPhone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    addressinformationsource = models.CharField(db_column='AddressInformationSource', max_length=30, blank=True, null=True)  # Field name made lowercase.
    webaddress = models.CharField(db_column='WebAddress', max_length=30, blank=True, null=True)  # Field name made lowercase.
    specialhandlingcode = models.CharField(db_column='SpecialHandlingCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    multilocationaccountflag = models.CharField(db_column='MultiLocationAccountFlag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    peoflag = models.CharField(db_column='PEOFlag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    disabilityofferingtaxstatus = models.CharField(db_column='DisabilityOfferingTaxStatus', max_length=30, blank=True, null=True)  # Field name made lowercase.
    transitoneflag = models.CharField(db_column='TransitOneFlag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    hsaflag = models.CharField(db_column='HSAFlag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    hraflag = models.CharField(db_column='HRAFlag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dataconfidencelevel = models.CharField(db_column='DataConfidenceLevel', max_length=30, blank=True, null=True)  # Field name made lowercase.
    totalpolicycount = models.IntegerField(db_column='TotalPolicyCount', blank=True, null=True)  # Field name made lowercase.
    pendingannualizedpremium = models.IntegerField(db_column='PendingAnnualizedPremium', blank=True, null=True)  # Field name made lowercase.
    percentbylineofbusiness = models.IntegerField(db_column='PercentByLineOfBusiness', blank=True, null=True)  # Field name made lowercase.
    scheduledlapsedate = models.DateTimeField(db_column='ScheduledLapseDate', blank=True, null=True)  # Field name made lowercase.
    penetrationpercentage = models.IntegerField(db_column='PenetrationPercentage', blank=True, null=True)  # Field name made lowercase.
    nofsaparticipants = models.IntegerField(db_column='NoFSAParticipants', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Account'
        unique_together = (('accountname', 'accountname2', 'locationaddress1', 'locationaddress2', 'locationcity', 'locationstate', 'locationzip', 'companycode'),)


class Accountmember(models.Model):
    custlastname = models.OneToOneField('Customer', models.DO_NOTHING, related_name="%(class)s_1069", db_column='CustLastName', primary_key=True)  # Field name made lowercase.
    custfirstname = models.ForeignKey('Customer', models.DO_NOTHING, related_name="%(class)s_1070", db_column='CustFirstName')  # Field name made lowercase.
    custmiddleinitial = models.ForeignKey('Customer', models.DO_NOTHING, related_name="%(class)s_1071", db_column='CustMiddleInitial')  # Field name made lowercase.
    custsuffix = models.ForeignKey('Customer', models.DO_NOTHING, related_name="%(class)s_1072", db_column='CustSuffix')  # Field name made lowercase.
    custdob = models.ForeignKey('Customer', models.DO_NOTHING, related_name="%(class)s_1073", db_column='CustDOB')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    accountname = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1075", db_column='AccountName')  # Field name made lowercase.
    accountname2 = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1076", db_column='AccountName2')  # Field name made lowercase.
    locationaddress1 = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1077", db_column='LocationAddress1')  # Field name made lowercase.
    locationaddress2 = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1078", db_column='LocationAddress2')  # Field name made lowercase.
    locationcity = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1079", db_column='LocationCity')  # Field name made lowercase.
    locationstate = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1080", db_column='LocationState')  # Field name made lowercase.
    locationzip = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1081", db_column='LocationZip')  # Field name made lowercase.
    companycode = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1082", db_column='CompanyCode')  # Field name made lowercase.
    fsacontributionamount = models.IntegerField(db_column='FSAContributionAmount', blank=True, null=True)  # Field name made lowercase.
    custbacctdepartmentname = models.CharField(db_column='CustBAcctDepartmentName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountMember'
        unique_together = (('custlastname', 'custfirstname', 'custmiddleinitial', 'custsuffix', 'custdob', 'accountname', 'accountname2', 'locationaddress1', 'locationaddress2', 'locationcity', 'locationstate', 'locationzip', 'companycode', 'startdate'),)


class AccountAssociate(models.Model):
    sitcode = models.OneToOneField('Managercontract', models.DO_NOTHING, related_name="%(class)s_1094", db_column='SitCode', primary_key=True)  # Field name made lowercase.
    companycode = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1095", db_column='CompanyCode')  # Field name made lowercase.
    writingnumber = models.ForeignKey('Managercontract', models.DO_NOTHING, related_name="%(class)s_1096", db_column='WritingNumber')  # Field name made lowercase.
    contractlevel = models.ForeignKey('Managercontract', models.DO_NOTHING, related_name="%(class)s_1097", db_column='ContractLevel')  # Field name made lowercase.
    issuedate = models.ForeignKey('Managercontract', models.DO_NOTHING, related_name="%(class)s_1098", db_column='IssueDate')  # Field name made lowercase.
    accountname = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1099", db_column='AccountName')  # Field name made lowercase.
    accountname2 = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1100", db_column='AccountName2')  # Field name made lowercase.
    locationaddress1 = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1101", db_column='LocationAddress1')  # Field name made lowercase.
    locationaddress2 = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1102", db_column='LocationAddress2')  # Field name made lowercase.
    locationcity = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1103", db_column='LocationCity')  # Field name made lowercase.
    locationstate = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1104", db_column='LocationState')  # Field name made lowercase.
    locationzip = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1105", db_column='LocationZip')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    associaterole = models.CharField(db_column='AssociateRole', max_length=30, blank=True, null=True)  # Field name made lowercase.
    stopdate = models.DateTimeField(db_column='StopDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Account_Associate'
        unique_together = (('sitcode', 'companycode', 'companycode', 'writingnumber', 'contractlevel', 'issuedate', 'accountname', 'accountname2', 'locationaddress1', 'locationaddress2', 'locationcity', 'locationstate', 'locationzip'),)


class AccountBillingaccount(models.Model):
    accountname = models.OneToOneField(Account, models.DO_NOTHING, related_name="%(class)s_1117", db_column='AccountName', primary_key=True)  # Field name made lowercase.
    accountname2 = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1118", db_column='AccountName2')  # Field name made lowercase.
    locationaddress1 = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1119", db_column='LocationAddress1')  # Field name made lowercase.
    locationaddress2 = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1120", db_column='LocationAddress2')  # Field name made lowercase.
    locationcity = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1121", db_column='LocationCity')  # Field name made lowercase.
    locationstate = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1122", db_column='LocationState')  # Field name made lowercase.
    locationzip = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1123", db_column='LocationZip')  # Field name made lowercase.
    companycode = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1124", db_column='CompanyCode')  # Field name made lowercase.
    bacctname = models.ForeignKey('Billingaccount', models.DO_NOTHING, related_name="%(class)s_1125", db_column='BAcctName')  # Field name made lowercase.
    bacctname2 = models.ForeignKey('Billingaccount', models.DO_NOTHING, related_name="%(class)s_1126", db_column='BAcctName2')  # Field name made lowercase.
    billingaddress1 = models.ForeignKey('Billingaccount', models.DO_NOTHING, related_name="%(class)s_1127", db_column='BillingAddress1')  # Field name made lowercase.
    billingaddress2 = models.ForeignKey('Billingaccount', models.DO_NOTHING, related_name="%(class)s_1128", db_column='BillingAddress2')  # Field name made lowercase.
    billingcity = models.ForeignKey('Billingaccount', models.DO_NOTHING, related_name="%(class)s_1129", db_column='BillingCity')  # Field name made lowercase.
    billingstate = models.ForeignKey('Billingaccount', models.DO_NOTHING, related_name="%(class)s_1130", db_column='BillingState')  # Field name made lowercase.
    billingzip = models.ForeignKey('Billingaccount', models.DO_NOTHING, related_name="%(class)s_1131", db_column='BillingZip')  # Field name made lowercase.
    relationshiptype = models.CharField(db_column='RelationshipType', max_length=30)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    billingfrequency = models.CharField(db_column='BillingFrequency', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nonbillablemonths = models.CharField(db_column='NonBillableMonths', max_length=30, blank=True, null=True)  # Field name made lowercase.
    enrollmentperiodlength = models.CharField(db_column='EnrollmentPeriodLength', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fsaclaimsreimbursementmethod = models.CharField(db_column='FSAClaimsReimbursementMethod', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fsaplantype = models.CharField(db_column='FSAPlanType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fsa_urmcap = models.CharField(db_column='FSA_URMCap', max_length=30, blank=True, null=True)  # Field name made lowercase.
    specificationcode = models.CharField(db_column='SpecificationCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    accounttype = models.CharField(db_column='AccountType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rcodeaccountflag = models.CharField(db_column='RCodeAccountFlag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rcodeassocflag = models.CharField(db_column='RCodeAssocFlag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rcodecustomerflag = models.CharField(db_column='RCodeCustomerFlag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    paymentcardflag = models.CharField(db_column='PaymentCardFlag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    departmentcode = models.CharField(db_column='DepartmentCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ficaexemptionflag = models.CharField(db_column='FICAExemptionFlag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    railroadtaxexemptionflag = models.CharField(db_column='RailroadTaxExemptionFlag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    contributionpercentage = models.CharField(db_column='ContributionPercentage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    highdeductiblemedicalpaymentplanflag = models.CharField(db_column='HighDeductibleMedicalPaymentPlanFlag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    medicalhealthinsuranceflag = models.CharField(db_column='MedicalHealthInsuranceFlag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    singlepointbillingflag = models.CharField(db_column='SinglePointBillingFlag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    expressreconciliationflag = models.CharField(db_column='ExpressReconciliationFlag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fsaservicefee = models.CharField(db_column='FSAServiceFee', max_length=30, blank=True, null=True)  # Field name made lowercase.
    graceperiodlength = models.CharField(db_column='GracePeriodLength', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Account_BillingAccount'
        unique_together = (('accountname', 'accountname2', 'locationaddress1', 'locationaddress2', 'locationcity', 'locationstate', 'locationzip', 'companycode', 'bacctname', 'bacctname2', 'billingaddress1', 'billingaddress2', 'billingcity', 'billingstate', 'billingzip', 'relationshiptype', 'startdate'),)


class AccountProductplan(models.Model):
    accountname = models.OneToOneField(Account, models.DO_NOTHING, related_name="%(class)s_1164", db_column='AccountName', primary_key=True)  # Field name made lowercase.
    accountname2 = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1165", db_column='AccountName2')  # Field name made lowercase.
    locationaddress1 = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1166", db_column='LocationAddress1')  # Field name made lowercase.
    locationaddress2 = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1167", db_column='LocationAddress2')  # Field name made lowercase.
    locationcity = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1168", db_column='LocationCity')  # Field name made lowercase.
    locationstate = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1169", db_column='LocationState')  # Field name made lowercase.
    locationzip = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1170", db_column='LocationZip')  # Field name made lowercase.
    companycode = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1171", db_column='CompanyCode')  # Field name made lowercase.
    lineofbusiness = models.ForeignKey('Productplan', models.DO_NOTHING, related_name="%(class)s_1172", db_column='LineOfBusiness')  # Field name made lowercase.
    seriesname = models.ForeignKey('Productplan', models.DO_NOTHING, related_name="%(class)s_1173", db_column='SeriesName')  # Field name made lowercase.
    planname = models.ForeignKey('Productplan', models.DO_NOTHING, related_name="%(class)s_1174", db_column='PlanName')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Account_ProductPlan'
        unique_together = (('accountname', 'accountname2', 'locationaddress1', 'locationaddress2', 'locationcity', 'locationstate', 'locationzip', 'companycode', 'lineofbusiness', 'seriesname', 'planname', 'startdate'),)


class Associate(models.Model):
    assoclastname = models.CharField(db_column='AssocLastName', primary_key=True, max_length=30)  # Field name made lowercase.
    assocfirstname = models.CharField(db_column='AssocFirstName', max_length=30)  # Field name made lowercase.
    assocmiddleinitial = models.CharField(db_column='AssocMiddleInitial', max_length=30)  # Field name made lowercase.
    assocsuffix = models.CharField(db_column='AssocSuffix', max_length=30)  # Field name made lowercase.
    assocdob = models.DateTimeField(db_column='AssocDOB')  # Field name made lowercase.
    tenuredate = models.DateTimeField(db_column='TenureDate', blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Associate'
        unique_together = (('assoclastname', 'assocfirstname', 'assocmiddleinitial', 'assocsuffix', 'assocdob'),)


class Benefitpremiumpredictionmodel(models.Model):
    dataurl = models.CharField(db_column='DataURL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    modelscripturl = models.CharField(db_column='ModelScriptURL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    benefitname = models.CharField(db_column='BenefitName', primary_key=True, max_length=30)  # Field name made lowercase.
    expectedexpenditure = models.FloatField(db_column='ExpectedExpenditure', blank=True, null=True)  # Field name made lowercase.
    savedmodelurl = models.CharField(db_column='SavedModelURL', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BenefitPremiumPredictionModel'


class Billingaccount(models.Model):
    bacctname = models.CharField(db_column='BAcctName', primary_key=True, max_length=30)  # Field name made lowercase.
    bacctname2 = models.CharField(db_column='BAcctName2', max_length=30)  # Field name made lowercase.
    billingaddress1 = models.CharField(db_column='BillingAddress1', max_length=30)  # Field name made lowercase.
    billingaddress2 = models.CharField(db_column='BillingAddress2', max_length=30)  # Field name made lowercase.
    billingcity = models.CharField(db_column='BillingCity', max_length=30)  # Field name made lowercase.
    billingstate = models.CharField(db_column='BillingState', max_length=30)  # Field name made lowercase.
    billingzip = models.CharField(db_column='BillingZip', max_length=30)  # Field name made lowercase.
    groupnumber = models.IntegerField(db_column='GroupNumber', blank=True, null=True)  # Field name made lowercase.
    taxidnumber = models.CharField(db_column='TaxIDNumber', max_length=30, blank=True, null=True)  # Field name made lowercase.
    onlinebillingflag = models.CharField(db_column='OnlineBillingFlag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    activitystatus = models.CharField(db_column='ActivityStatus', max_length=30, blank=True, null=True)  # Field name made lowercase.
    activitystatusdate = models.DateTimeField(db_column='ActivityStatusDate', blank=True, null=True)  # Field name made lowercase.
    webaddress = models.CharField(db_column='WebAddress', max_length=30, blank=True, null=True)  # Field name made lowercase.
    payrollprocessorflag = models.CharField(db_column='PayrollProcessorFlag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    billingphone = models.CharField(db_column='BillingPhone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    billingaccttypedate = models.DateTimeField(db_column='BillingAcctTypeDate', blank=True, null=True)  # Field name made lowercase.
    specialhandlingcode = models.CharField(db_column='SpecialHandlingCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    changefilesflag = models.CharField(db_column='ChangeFilesFlag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    enrollmentfileflag = models.CharField(db_column='EnrollmentFileFlag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    debitcardflag = models.CharField(db_column='DebitCardFlag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    billingfileflag = models.CharField(db_column='BillingFileFlag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ftpsite = models.CharField(db_column='FTPSite', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nextvisitdate = models.DateTimeField(db_column='NextVisitDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BillingAccount'
        unique_together = (('bacctname', 'bacctname2', 'billingaddress1', 'billingaddress2', 'billingcity', 'billingstate', 'billingzip'),)


class Claim(models.Model):
    claimnumber = models.IntegerField(db_column='ClaimNumber', primary_key=True)  # Field name made lowercase.
    claimdate = models.DateTimeField(db_column='ClaimDate', blank=True, null=True)  # Field name made lowercase.
    settlementdate = models.DateTimeField(db_column='SettlementDate', blank=True, null=True)  # Field name made lowercase.
    wellnesseligibilitydate = models.DateTimeField(db_column='WellnessEligibilityDate', blank=True, null=True)  # Field name made lowercase.
    contractnumber = models.ForeignKey('Contract', models.DO_NOTHING, related_name="%(class)s_1247", db_column='ContractNumber')  # Field name made lowercase.
    lineofbusiness = models.ForeignKey('Contract', models.DO_NOTHING, related_name="%(class)s_1248", db_column='LineOfBusiness')  # Field name made lowercase.
    seriesname = models.ForeignKey('Contract', models.DO_NOTHING, related_name="%(class)s_1249", db_column='SeriesName')  # Field name made lowercase.
    planname = models.ForeignKey('Contract', models.DO_NOTHING, related_name="%(class)s_1250", db_column='PlanName')  # Field name made lowercase.
    claimnote = models.CharField(db_column='ClaimNote', max_length=30, blank=True, null=True)  # Field name made lowercase.
    custlastname = models.ForeignKey('Customer', models.DO_NOTHING, related_name="%(class)s_1252", db_column='CustLastName')  # Field name made lowercase.
    custfirstname = models.ForeignKey('Customer', models.DO_NOTHING, related_name="%(class)s_1253", db_column='CustFirstName')  # Field name made lowercase.
    custmiddleinitial = models.ForeignKey('Customer', models.DO_NOTHING, related_name="%(class)s_1254", db_column='CustMiddleInitial')  # Field name made lowercase.
    custsuffix = models.ForeignKey('Customer', models.DO_NOTHING, related_name="%(class)s_1255", db_column='CustSuffix')  # Field name made lowercase.
    custdob = models.ForeignKey('Customer', models.DO_NOTHING, related_name="%(class)s_1256", db_column='CustDOB')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Claim'
        unique_together = (('claimnumber', 'contractnumber', 'lineofbusiness', 'seriesname', 'planname', 'custlastname', 'custfirstname', 'custmiddleinitial', 'custsuffix', 'custdob'),)


class Claimevent(models.Model):
    finame = models.ForeignKey('Financialinstitution', models.DO_NOTHING, related_name="%(class)s_1265", db_column='FIName')  # Field name made lowercase.
    fiaddress1 = models.ForeignKey('Financialinstitution', models.DO_NOTHING, related_name="%(class)s_1266", db_column='FIAddress1')  # Field name made lowercase.
    fiaddress2 = models.ForeignKey('Financialinstitution', models.DO_NOTHING, related_name="%(class)s_1267", db_column='FIAddress2')  # Field name made lowercase.
    fincity = models.ForeignKey('Financialinstitution', models.DO_NOTHING, related_name="%(class)s_1268", db_column='FINCity')  # Field name made lowercase.
    finstate = models.ForeignKey('Financialinstitution', models.DO_NOTHING, related_name="%(class)s_1269", db_column='FINState')  # Field name made lowercase.
    finzip = models.ForeignKey('Financialinstitution', models.DO_NOTHING, related_name="%(class)s_1270", db_column='FINZip')  # Field name made lowercase.
    fiphone = models.ForeignKey('Financialinstitution', models.DO_NOTHING, related_name="%(class)s_1271", db_column='FIPhone')  # Field name made lowercase.
    claimnumber = models.OneToOneField(Claim, models.DO_NOTHING, related_name="%(class)s_1272", db_column='ClaimNumber', primary_key=True)  # Field name made lowercase.
    contractnumber = models.ForeignKey(Claim, models.DO_NOTHING, related_name="%(class)s_1273", db_column='ContractNumber')  # Field name made lowercase.
    lineofbusiness = models.ForeignKey(Claim, models.DO_NOTHING, related_name="%(class)s_1274", db_column='LineOfBusiness')  # Field name made lowercase.
    seriesname = models.ForeignKey(Claim, models.DO_NOTHING, related_name="%(class)s_1275", db_column='SeriesName')  # Field name made lowercase.
    planname = models.ForeignKey(Claim, models.DO_NOTHING, related_name="%(class)s_1276", db_column='PlanName')  # Field name made lowercase.
    custlastname = models.ForeignKey(Claim, models.DO_NOTHING, related_name="%(class)s_1277", db_column='CustLastName')  # Field name made lowercase.
    custfirstname = models.ForeignKey(Claim, models.DO_NOTHING, related_name="%(class)s_1278", db_column='CustFirstName')  # Field name made lowercase.
    custmiddleinitial = models.ForeignKey(Claim, models.DO_NOTHING, related_name="%(class)s_1279", db_column='CustMiddleInitial')  # Field name made lowercase.
    custsuffix = models.ForeignKey(Claim, models.DO_NOTHING, related_name="%(class)s_1280", db_column='CustSuffix')  # Field name made lowercase.
    custdob = models.ForeignKey(Claim, models.DO_NOTHING, related_name="%(class)s_1281", db_column='CustDOB')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClaimEvent'
        unique_together = (('claimnumber', 'contractnumber', 'lineofbusiness', 'seriesname', 'planname', 'finame', 'fiaddress1', 'fiaddress2', 'fincity', 'finstate', 'finzip', 'fiphone', 'custlastname', 'custfirstname', 'custmiddleinitial', 'custsuffix', 'custdob'),)


class Claimimage(models.Model):
    claimnumber = models.OneToOneField(Claim, models.DO_NOTHING, related_name="%(class)s_1290", db_column='ClaimNumber', primary_key=True)  # Field name made lowercase.
    documentid = models.IntegerField(db_column='DocumentId')  # Field name made lowercase.
    documentclass = models.CharField(db_column='DocumentClass', max_length=30, blank=True, null=True)  # Field name made lowercase.
    imagetype = models.CharField(db_column='ImageType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    datereceived = models.DateTimeField(db_column='DateReceived', blank=True, null=True)  # Field name made lowercase.
    processeddate = models.DateTimeField(db_column='ProcessedDate', blank=True, null=True)  # Field name made lowercase.
    contractnumber = models.ForeignKey(Claim, models.DO_NOTHING, related_name="%(class)s_1296", db_column='ContractNumber')  # Field name made lowercase.
    lineofbusiness = models.ForeignKey(Claim, models.DO_NOTHING, related_name="%(class)s_1297", db_column='LineOfBusiness')  # Field name made lowercase.
    seriesname = models.ForeignKey(Claim, models.DO_NOTHING, related_name="%(class)s_1298", db_column='SeriesName')  # Field name made lowercase.
    planname = models.ForeignKey(Claim, models.DO_NOTHING, related_name="%(class)s_1299", db_column='PlanName')  # Field name made lowercase.
    custlastname = models.ForeignKey(Claim, models.DO_NOTHING, related_name="%(class)s_1300", db_column='CustLastName')  # Field name made lowercase.
    custfirstname = models.ForeignKey(Claim, models.DO_NOTHING, related_name="%(class)s_1301", db_column='CustFirstName')  # Field name made lowercase.
    custmiddleinitial = models.ForeignKey(Claim, models.DO_NOTHING, related_name="%(class)s_1302", db_column='CustMiddleInitial')  # Field name made lowercase.
    custsuffix = models.ForeignKey(Claim, models.DO_NOTHING, related_name="%(class)s_1303", db_column='CustSuffix')  # Field name made lowercase.
    custdob = models.ForeignKey(Claim, models.DO_NOTHING, related_name="%(class)s_1304", db_column='CustDOB')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClaimImage'
        unique_together = (('claimnumber', 'documentid', 'contractnumber', 'lineofbusiness', 'seriesname', 'planname', 'custlastname', 'custfirstname', 'custmiddleinitial', 'custsuffix', 'custdob'),)


class Contract(models.Model):
    contractnumber = models.CharField(db_column='ContractNumber', primary_key=True, max_length=30)  # Field name made lowercase.
    lineofbusiness = models.ForeignKey('Productplan', models.DO_NOTHING, related_name="%(class)s_1314", db_column='LineOfBusiness')  # Field name made lowercase.
    seriesname = models.ForeignKey('Productplan', models.DO_NOTHING, related_name="%(class)s_1315", db_column='SeriesName')  # Field name made lowercase.
    planname = models.ForeignKey('Productplan', models.DO_NOTHING, related_name="%(class)s_1316", db_column='PlanName')  # Field name made lowercase.
    activitystatus = models.CharField(db_column='ActivityStatus', max_length=30, blank=True, null=True)  # Field name made lowercase.
    activitystatusdate = models.DateTimeField(db_column='ActivityStatusDate', blank=True, null=True)  # Field name made lowercase.
    coveragetype = models.CharField(db_column='CoverageType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    billingmethod = models.CharField(db_column='BillingMethod', max_length=30, blank=True, null=True)  # Field name made lowercase.
    accountname = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1321", db_column='AccountName', blank=True, null=True)  # Field name made lowercase.
    accountname2 = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1322", db_column='AccountName2', blank=True, null=True)  # Field name made lowercase.
    locationaddress1 = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1323", db_column='LocationAddress1', blank=True, null=True)  # Field name made lowercase.
    locationaddress2 = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1324", db_column='LocationAddress2', blank=True, null=True)  # Field name made lowercase.
    locationcity = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1325", db_column='LocationCity', blank=True, null=True)  # Field name made lowercase.
    locationstate = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1326", db_column='LocationState', blank=True, null=True)  # Field name made lowercase.
    locationzip = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1327", db_column='LocationZip', blank=True, null=True)  # Field name made lowercase.
    companycode = models.ForeignKey(Account, models.DO_NOTHING, related_name="%(class)s_1328", db_column='CompanyCode', blank=True, null=True)  # Field name made lowercase.
    individualcompanycode = models.CharField(db_column='IndividualCompanyCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    suspendcode = models.CharField(db_column='SuspendCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    exceptioncode = models.CharField(db_column='ExceptionCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    modalpremium = models.CharField(db_column='ModalPremium', max_length=30, blank=True, null=True)  # Field name made lowercase.
    autopremiumloan = models.CharField(db_column='AutoPremiumLoan', max_length=30, blank=True, null=True)  # Field name made lowercase.
    creditcardno = models.CharField(db_column='CreditCardNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    expirationdate = models.DateTimeField(db_column='ExpirationDate', blank=True, null=True)  # Field name made lowercase.
    cardtype = models.CharField(db_column='CardType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bankingtransitnumber = models.CharField(db_column='BankingTransitNumber', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bankingaccounttype = models.CharField(db_column='BankingAccountType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bankingaccountnumber = models.CharField(db_column='BankingAccountNumber', max_length=30, blank=True, null=True)  # Field name made lowercase.
    premiumpaymentlimit = models.CharField(db_column='PremiumPaymentLimit', max_length=30, blank=True, null=True)  # Field name made lowercase.
    substandardrate = models.CharField(db_column='SubstandardRate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    valuationinterestcode = models.CharField(db_column='ValuationInterestCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    supplementalbenefitplan = models.CharField(db_column='SupplementalBenefitPlan', max_length=30, blank=True, null=True)  # Field name made lowercase.
    specialassemblycode = models.CharField(db_column='SpecialAssemblyCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    inforceflag = models.CharField(db_column='InForceFlag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    payupdate = models.DateTimeField(db_column='PayUpDate', blank=True, null=True)  # Field name made lowercase.
    duration = models.CharField(db_column='Duration', max_length=30, blank=True, null=True)  # Field name made lowercase.
    contractlanguage = models.CharField(db_column='ContractLanguage', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contract'
        unique_together = (('contractnumber', 'lineofbusiness', 'seriesname', 'planname'),)


class Contractbenefit(models.Model):
    contractnumber = models.OneToOneField(Contract, models.DO_NOTHING, related_name="%(class)s_1357", db_column='ContractNumber', primary_key=True)  # Field name made lowercase.
    lineofbusiness = models.ForeignKey('Productplan', models.DO_NOTHING, related_name="%(class)s_1358", db_column='LineOfBusiness')  # Field name made lowercase.
    seriesname = models.ForeignKey('Productplan', models.DO_NOTHING, related_name="%(class)s_1359", db_column='SeriesName')  # Field name made lowercase.
    planname = models.ForeignKey('Productplan', models.DO_NOTHING, related_name="%(class)s_1360", db_column='PlanName')  # Field name made lowercase.
    policycountcontribution = models.CharField(db_column='PolicyCountContribution', max_length=30, blank=True, null=True)  # Field name made lowercase.
    benefitname = models.ForeignKey(Benefitpremiumpredictionmodel, models.DO_NOTHING, related_name="%(class)s_1362", db_column='BenefitName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContractBenefit'
        unique_together = (('contractnumber', 'lineofbusiness', 'lineofbusiness', 'seriesname', 'seriesname', 'planname', 'planname', 'benefitname'),)


class Contractpremium(models.Model):
    contractnumber = models.OneToOneField(Contractbenefit, models.DO_NOTHING, related_name="%(class)s_1371", db_column='ContractNumber', primary_key=True)  # Field name made lowercase.
    lineofbusiness = models.ForeignKey(Contractbenefit, models.DO_NOTHING, related_name="%(class)s_1372", db_column='LineOfBusiness')  # Field name made lowercase.
    seriesname = models.ForeignKey(Contractbenefit, models.DO_NOTHING, related_name="%(class)s_1373", db_column='SeriesName')  # Field name made lowercase.
    planname = models.ForeignKey(Contractbenefit, models.DO_NOTHING, related_name="%(class)s_1374", db_column='PlanName')  # Field name made lowercase.
    premiumcode = models.CharField(db_column='PremiumCode', max_length=30)  # Field name made lowercase.
    annualizedpremium = models.IntegerField(db_column='AnnualizedPremium', blank=True, null=True)  # Field name made lowercase.
    processdate = models.DateTimeField(db_column='ProcessDate', blank=True, null=True)  # Field name made lowercase.
    appsigndate = models.DateTimeField(db_column='AppSignDate', blank=True, null=True)  # Field name made lowercase.
    benefitname = models.ForeignKey(Contractbenefit, models.DO_NOTHING, related_name="%(class)s_1379", db_column='BenefitName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContractPremium'
        unique_together = (('contractnumber', 'lineofbusiness', 'seriesname', 'planname', 'premiumcode', 'benefitname'),)


class Contractingparty(models.Model):
    contractnumber = models.OneToOneField(Contract, models.DO_NOTHING, related_name="%(class)s_1388", db_column='ContractNumber', primary_key=True)  # Field name made lowercase.
    lineofbusiness = models.ForeignKey(Contract, models.DO_NOTHING, related_name="%(class)s_1389", db_column='LineOfBusiness')  # Field name made lowercase.
    seriesname = models.ForeignKey(Contract, models.DO_NOTHING, related_name="%(class)s_1390", db_column='SeriesName')  # Field name made lowercase.
    planname = models.ForeignKey(Contract, models.DO_NOTHING, related_name="%(class)s_1391", db_column='PlanName')  # Field name made lowercase.
    custfirstname = models.ForeignKey('Customer', models.DO_NOTHING, related_name="%(class)s_1392", db_column='CustFirstName')  # Field name made lowercase.
    custmiddleinitial = models.ForeignKey('Customer', models.DO_NOTHING, related_name="%(class)s_1393", db_column='CustMiddleInitial')  # Field name made lowercase.
    custsuffix = models.ForeignKey('Customer', models.DO_NOTHING, related_name="%(class)s_1394", db_column='CustSuffix')  # Field name made lowercase.
    custdob = models.ForeignKey('Customer', models.DO_NOTHING, related_name="%(class)s_1395", db_column='CustDOB')  # Field name made lowercase.
    custlastname = models.ForeignKey('Customer', models.DO_NOTHING, related_name="%(class)s_1396", db_column='CustLastName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContractingParty'
        unique_together = (('contractnumber', 'lineofbusiness', 'seriesname', 'planname', 'custfirstname', 'custmiddleinitial', 'custsuffix', 'custdob', 'custlastname'),)


class Criticalinsurancedata(models.Model):
    custfirstname = models.OneToOneField('Customer', models.DO_NOTHING, related_name="%(class)s_1405", db_column='CustFirstName', primary_key=True)  # Field name made lowercase.
    custmiddleinitial = models.CharField(blank=True, null=True, max_length=30, db_column='CustMiddleInitial')  # Field name made lowercase.
    custsuffix = models.CharField(db_column='CustSuffix', blank=True, null=True, max_length=30)  # Field name made lowercase.
    custdob = models.DateTimeField(db_column='CustDOB')  # Field name made lowercase.
    custlastname = models.CharField(blank=True, null=True, max_length=30, db_column='CustLastName')  # Field name made lowercase.
    
    assessmentdate = models.DateTimeField(db_column='AssessmentDate')  # Field name made lowercase.
    lastassessmentflag = models.BooleanField(db_column='LastAssessmentFlag', blank=True, null=True)  # Field name made lowercase.
    hypertensionflag = models.BooleanField(db_column='HypertensionFlag', blank=True, null=True)  # Field name made lowercase.
    prevheartdiseaseflag = models.BooleanField(db_column='PrevHeartDiseaseFlag', blank=True, null=True)  # Field name made lowercase.
    worktype = models.CharField(db_column='WorkType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    urbanresidenceflag = models.BooleanField(db_column='UrbanResidenceFlag', blank=True, null=True)  # Field name made lowercase.
    avgglucoselevel = models.FloatField(db_column='AvgGlucoseLevel', blank=True, null=True)  # Field name made lowercase.
    prevstrokeflag = models.BooleanField(db_column='PrevStrokeFlag', blank=True, null=True)  # Field name made lowercase.
    alcoholflag = models.BooleanField(db_column='AlcoholFlag', blank=True, null=True)  # Field name made lowercase.
    physicalhealthscore = models.IntegerField(db_column='PhysicalHealthScore', blank=True, null=True)  # Field name made lowercase.
    mentalhealthscore = models.IntegerField(db_column='MentalHealthScore', blank=True, null=True)  # Field name made lowercase.
    diffwalkingflag = models.BooleanField(db_column='DiffWalkingFlag', blank=True, null=True)  # Field name made lowercase.
    diabeticflag = models.BooleanField(db_column='DiabeticFlag', blank=True, null=True)  # Field name made lowercase.
    physicalactivityflag = models.BooleanField(db_column='PhysicalActivityFlag', blank=True, null=True)  # Field name made lowercase.
    sleeptime = models.IntegerField(db_column='SleepTime', blank=True, null=True)  # Field name made lowercase.
    asthmaflag = models.BooleanField(db_column='AsthmaFlag', blank=True, null=True)  # Field name made lowercase.
    kidneydiseaseflag = models.BooleanField(db_column='KidneyDiseaseFlag', blank=True, null=True)  # Field name made lowercase.
    skincancerflag = models.BooleanField(db_column='SkinCancerFlag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CriticalInsuranceData'
        unique_together = (('custfirstname', 'custmiddleinitial', 'custsuffix', 'custdob', 'custlastname', 'assessmentdate'),)


class Customer(models.Model):
    custfirstname = models.CharField(db_column='CustFirstName', primary_key=True, max_length=30)  # Field name made lowercase.
    custmiddleinitial = models.CharField(db_column='CustMiddleInitial', max_length=30)  # Field name made lowercase.
    custsuffix = models.CharField(db_column='CustSuffix', max_length=30)  # Field name made lowercase.
    custdob = models.DateTimeField(db_column='CustDOB')  # Field name made lowercase.
    custsalutation = models.CharField(db_column='CustSalutation', max_length=30, blank=True, null=True)  # Field name made lowercase.
    custemailaddress = models.CharField(db_column='CusteMailAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ssn_tin = models.CharField(db_column='SSN_TIN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ssn_type = models.CharField(db_column='SSN_Type', max_length=30, blank=True, null=True)  # Field name made lowercase.
    custlastname = models.CharField(db_column='CustLastName', max_length=30)  # Field name made lowercase.
    preferredlanguage = models.CharField(db_column='PreferredLanguage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    bmi = models.FloatField(db_column='BMI', blank=True, null=True)  # Field name made lowercase.
    numchildren = models.IntegerField(db_column='NumChildren', blank=True, null=True)  # Field name made lowercase.
    evermarriedflag = models.BooleanField(db_column='EverMarriedFlag', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=30, blank=True, null=True)  # Field name made lowercase.
    smokerflag = models.BooleanField(db_column='SmokerFlag', blank=True, null=True)  # Field name made lowercase.
    lastassessmentdate = models.DateTimeField(db_column='LastAssessmentDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customer'
        unique_together = (('ssn_tin', 'ssn_type'), ('custfirstname', 'custmiddleinitial', 'custsuffix', 'custdob', 'custlastname'),)


class Customeraddress(models.Model):
    custlastname = models.OneToOneField(Customer, models.DO_NOTHING, related_name="%(class)s_1462", db_column='CustLastName', primary_key=True)  # Field name made lowercase.
    custfirstname = models.ForeignKey(Customer, models.DO_NOTHING, related_name="%(class)s_1463", db_column='CustFirstName')  # Field name made lowercase.
    custmiddleinitial = models.ForeignKey(Customer, models.DO_NOTHING, related_name="%(class)s_1464", db_column='CustMiddleInitial')  # Field name made lowercase.
    custsuffix = models.ForeignKey(Customer, models.DO_NOTHING, related_name="%(class)s_1465", db_column='CustSuffix')  # Field name made lowercase.
    custdob = models.ForeignKey(Customer, models.DO_NOTHING, related_name="%(class)s_1466", db_column='CustDOB')  # Field name made lowercase.
    custaddress2 = models.CharField(db_column='CustAddress2', max_length=30)  # Field name made lowercase.
    custaddress1 = models.CharField(db_column='CustAddress1', max_length=30)  # Field name made lowercase.
    custcity = models.CharField(db_column='CustCity', max_length=30)  # Field name made lowercase.
    custstate = models.ForeignKey('Stateregions', models.DO_NOTHING, related_name="%(class)s_1470", db_column='CustState')  # Field name made lowercase.
    custzip = models.CharField(db_column='CustZip', max_length=30)  # Field name made lowercase.
    annualstartdate = models.DateTimeField(db_column='AnnualStartDate')  # Field name made lowercase.
    annualenddate = models.DateTimeField(db_column='AnnualEndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CustomerAddress'
        unique_together = (('custlastname', 'custfirstname', 'custmiddleinitial', 'custsuffix', 'custdob', 'custaddress1', 'custaddress2', 'custcity', 'custstate', 'custzip', 'annualstartdate'),)


class Financialinstitution(models.Model):
    finame = models.CharField(db_column='FIName', primary_key=True, max_length=30)  # Field name made lowercase.
    fiaddress1 = models.CharField(db_column='FIAddress1', max_length=30)  # Field name made lowercase.
    fiaddress2 = models.CharField(db_column='FIAddress2', max_length=30)  # Field name made lowercase.
    fincity = models.CharField(db_column='FINCity', max_length=30)  # Field name made lowercase.
    finstate = models.CharField(db_column='FINState', max_length=30)  # Field name made lowercase.
    finzip = models.CharField(db_column='FINZip', max_length=30)  # Field name made lowercase.
    fiphone = models.CharField(db_column='FIPhone', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FinancialInstitution'
        unique_together = (('finame', 'fiaddress1', 'fiaddress2', 'fincity', 'finstate', 'finzip', 'fiphone'),)


class Invoice(models.Model):
    invoicenumber = models.IntegerField(db_column='InvoiceNumber', primary_key=True)  # Field name made lowercase.
    custlastname = models.ForeignKey(Customer, models.DO_NOTHING, related_name="%(class)s_1498", db_column='CustLastName', blank=True, null=True)  # Field name made lowercase.
    custfirstname = models.ForeignKey(Customer, models.DO_NOTHING, related_name="%(class)s_1499", db_column='CustFirstName', blank=True, null=True)  # Field name made lowercase.
    custmiddleinitial = models.ForeignKey(Customer, models.DO_NOTHING, related_name="%(class)s_1500", db_column='CustMiddleInitial', blank=True, null=True)  # Field name made lowercase.
    custsuffix = models.ForeignKey(Customer, models.DO_NOTHING, related_name="%(class)s_1501", db_column='CustSuffix', blank=True, null=True)  # Field name made lowercase.
    custdob = models.ForeignKey(Customer, models.DO_NOTHING, related_name="%(class)s_1502", db_column='CustDOB', blank=True, null=True)  # Field name made lowercase.
    paiddate = models.DateTimeField(db_column='PaidDate', blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate', blank=True, null=True)  # Field name made lowercase.
    rundate = models.DateTimeField(db_column='RunDate', blank=True, null=True)  # Field name made lowercase.
    contractnumber = models.ForeignKey(Contract, models.DO_NOTHING, related_name="%(class)s_1506", db_column='ContractNumber')  # Field name made lowercase.
    lineofbusiness = models.ForeignKey(Contract, models.DO_NOTHING, related_name="%(class)s_1507", db_column='LineOfBusiness')  # Field name made lowercase.
    seriesname = models.ForeignKey(Contract, models.DO_NOTHING, related_name="%(class)s_1508", db_column='SeriesName')  # Field name made lowercase.
    planname = models.ForeignKey(Contract, models.DO_NOTHING, related_name="%(class)s_1509", db_column='PlanName')  # Field name made lowercase.
    bacctname = models.ForeignKey(Billingaccount, models.DO_NOTHING, related_name="%(class)s_1510", db_column='BAcctName')  # Field name made lowercase.
    bacctname2 = models.ForeignKey(Billingaccount, models.DO_NOTHING, related_name="%(class)s_1511", db_column='BAcctName2')  # Field name made lowercase.
    billingaddress1 = models.ForeignKey(Billingaccount, models.DO_NOTHING, related_name="%(class)s_1512", db_column='BillingAddress1')  # Field name made lowercase.
    billingaddress2 = models.ForeignKey(Billingaccount, models.DO_NOTHING, related_name="%(class)s_1513", db_column='BillingAddress2')  # Field name made lowercase.
    billingcity = models.ForeignKey(Billingaccount, models.DO_NOTHING, related_name="%(class)s_1514", db_column='BillingCity')  # Field name made lowercase.
    billingstate = models.ForeignKey(Billingaccount, models.DO_NOTHING, related_name="%(class)s_1515", db_column='BillingState')  # Field name made lowercase.
    billingzip = models.ForeignKey(Billingaccount, models.DO_NOTHING, related_name="%(class)s_1516", db_column='BillingZip')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Invoice'
        unique_together = (('invoicenumber', 'contractnumber', 'lineofbusiness', 'seriesname', 'planname', 'bacctname', 'bacctname2', 'billingaddress1', 'billingaddress2', 'billingcity', 'billingstate', 'billingzip'),)


class Managercontract(models.Model):
    sitcode = models.CharField(db_column='SitCode', primary_key=True, max_length=30)  # Field name made lowercase.
    companycode = models.CharField(db_column='CompanyCode', max_length=30)  # Field name made lowercase.
    writingnumber = models.IntegerField(db_column='WritingNumber')  # Field name made lowercase.
    issuedate = models.DateTimeField(db_column='IssueDate')  # Field name made lowercase.
    contracttype = models.CharField(db_column='ContractType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    contractsigndate = models.DateTimeField(db_column='ContractSignDate', blank=True, null=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='Datetime', blank=True, null=True)  # Field name made lowercase.
    contractprocessdate = models.DateTimeField(db_column='ContractProcessDate', blank=True, null=True)  # Field name made lowercase.
    parentsitcode = models.ForeignKey('self', models.DO_NOTHING, related_name="%(class)s_1533", db_column='ParentSitCode', blank=True, null=True)  # Field name made lowercase.
    parentcompanycode = models.ForeignKey('self', models.DO_NOTHING, related_name="%(class)s_1534", db_column='ParentCompanyCode', blank=True, null=True)  # Field name made lowercase.
    parentwritingnumber = models.ForeignKey('self', models.DO_NOTHING, related_name="%(class)s_1535", db_column='ParentWritingNumber', blank=True, null=True)  # Field name made lowercase.
    contractlevel = models.ForeignKey('self', models.DO_NOTHING, related_name="%(class)s_1536", db_column='ContractLevel')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    parentissuedate = models.ForeignKey('self', models.DO_NOTHING, related_name="%(class)s_1538", db_column='ParentIssueDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    assoclastname = models.ForeignKey(Associate, models.DO_NOTHING, related_name="%(class)s_1540", db_column='AssocLastName', blank=True, null=True)  # Field name made lowercase.
    assocfirstname = models.ForeignKey(Associate, models.DO_NOTHING, related_name="%(class)s_1541", db_column='AssocFirstName', blank=True, null=True)  # Field name made lowercase.
    assocmiddleinitial = models.ForeignKey(Associate, models.DO_NOTHING, related_name="%(class)s_1542", db_column='AssocMiddleInitial', blank=True, null=True)  # Field name made lowercase.
    assocsuffix = models.ForeignKey(Associate, models.DO_NOTHING, related_name="%(class)s_1543", db_column='AssocSuffix', blank=True, null=True)  # Field name made lowercase.
    assocdob = models.ForeignKey(Associate, models.DO_NOTHING, related_name="%(class)s_1544", db_column='AssocDOB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ManagerContract'
        unique_together = (('sitcode', 'companycode', 'writingnumber', 'issuedate', 'contractlevel'),)


class PremiumMgmtcontract(models.Model):
    contractnumber = models.OneToOneField(Contractpremium, models.DO_NOTHING, related_name="%(class)s_1553", db_column='ContractNumber', primary_key=True)  # Field name made lowercase.
    lineofbusiness = models.ForeignKey(Contractpremium, models.DO_NOTHING, related_name="%(class)s_1554", db_column='LineOfBusiness')  # Field name made lowercase.
    seriesname = models.ForeignKey(Contractpremium, models.DO_NOTHING, related_name="%(class)s_1555", db_column='SeriesName')  # Field name made lowercase.
    planname = models.ForeignKey(Contractpremium, models.DO_NOTHING, related_name="%(class)s_1556", db_column='PlanName')  # Field name made lowercase.
    premiumcode = models.ForeignKey(Contractpremium, models.DO_NOTHING, related_name="%(class)s_1557", db_column='PremiumCode')  # Field name made lowercase.
    sitcode = models.ForeignKey(Managercontract, models.DO_NOTHING, related_name="%(class)s_1558", db_column='SitCode')  # Field name made lowercase.
    companycode = models.ForeignKey(Managercontract, models.DO_NOTHING, related_name="%(class)s_1559", db_column='CompanyCode')  # Field name made lowercase.
    writingnumber = models.ForeignKey(Managercontract, models.DO_NOTHING, related_name="%(class)s_1560", db_column='WritingNumber')  # Field name made lowercase.
    contractlevel = models.ForeignKey(Managercontract, models.DO_NOTHING, related_name="%(class)s_1561", db_column='ContractLevel')  # Field name made lowercase.
    issuedate = models.ForeignKey(Managercontract, models.DO_NOTHING, related_name="%(class)s_1562", db_column='IssueDate')  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    commissionrate = models.CharField(db_column='CommissionRate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    benefitname = models.ForeignKey(Contractpremium, models.DO_NOTHING, related_name="%(class)s_1565", db_column='BenefitName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Premium_MgmtContract'
        unique_together = (('contractnumber', 'lineofbusiness', 'seriesname', 'planname', 'premiumcode', 'sitcode', 'companycode', 'writingnumber', 'contractlevel', 'issuedate', 'benefitname'),)


class Productplan(models.Model):
    lineofbusiness = models.CharField(db_column='LineOfBusiness', primary_key=True, max_length=30)  # Field name made lowercase.
    seriesname = models.CharField(db_column='SeriesName', max_length=30)  # Field name made lowercase.
    planname = models.CharField(db_column='PlanName', max_length=30)  # Field name made lowercase.
    ratebooklocationcode = models.CharField(db_column='RatebookLocationCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    plancode = models.CharField(db_column='PlanCode', unique=True, max_length=30, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductPlan'
        unique_together = (('lineofbusiness', 'seriesname', 'planname'),)


class Remittance(models.Model):
    finame = models.OneToOneField(Financialinstitution, models.DO_NOTHING, related_name="%(class)s_1588", db_column='FIName', primary_key=True)  # Field name made lowercase.
    fiaddress1 = models.ForeignKey(Financialinstitution, models.DO_NOTHING, related_name="%(class)s_1589", db_column='FIAddress1')  # Field name made lowercase.
    fiaddress2 = models.ForeignKey(Financialinstitution, models.DO_NOTHING, related_name="%(class)s_1590", db_column='FIAddress2')  # Field name made lowercase.
    fincity = models.ForeignKey(Financialinstitution, models.DO_NOTHING, related_name="%(class)s_1591", db_column='FINCity')  # Field name made lowercase.
    finstate = models.ForeignKey(Financialinstitution, models.DO_NOTHING, related_name="%(class)s_1592", db_column='FINState')  # Field name made lowercase.
    finzip = models.ForeignKey(Financialinstitution, models.DO_NOTHING, related_name="%(class)s_1593", db_column='FINZip')  # Field name made lowercase.
    fiphone = models.ForeignKey(Financialinstitution, models.DO_NOTHING, related_name="%(class)s_1594", db_column='FIPhone')  # Field name made lowercase.
    custfirstname = models.ForeignKey(Customer, models.DO_NOTHING, related_name="%(class)s_1595", db_column='CustFirstName', blank=True, null=True)  # Field name made lowercase.
    custmiddleinitial = models.ForeignKey(Customer, models.DO_NOTHING, related_name="%(class)s_1596", db_column='CustMiddleInitial', blank=True, null=True)  # Field name made lowercase.
    custdob = models.ForeignKey(Customer, models.DO_NOTHING, related_name="%(class)s_1597", db_column='CustDOB', blank=True, null=True)  # Field name made lowercase.
    custlastname = models.ForeignKey(Customer, models.DO_NOTHING, related_name="%(class)s_1598", db_column='CustLastName', blank=True, null=True)  # Field name made lowercase.
    contractnumber = models.ForeignKey(Contract, models.DO_NOTHING, related_name="%(class)s_1599", db_column='ContractNumber')  # Field name made lowercase.
    lineofbusiness = models.ForeignKey(Contract, models.DO_NOTHING, related_name="%(class)s_1600", db_column='LineOfBusiness')  # Field name made lowercase.
    seriesname = models.ForeignKey(Contract, models.DO_NOTHING, related_name="%(class)s_1601", db_column='SeriesName')  # Field name made lowercase.
    planname = models.ForeignKey(Contract, models.DO_NOTHING, related_name="%(class)s_1602", db_column='PlanName')  # Field name made lowercase.
    remittancefreq = models.CharField(db_column='RemittanceFreq', max_length=30, blank=True, null=True)  # Field name made lowercase.
    remittancedate = models.DateTimeField(db_column='RemittanceDate', blank=True, null=True)  # Field name made lowercase.
    paymentmethod = models.CharField(db_column='PaymentMethod', max_length=30, blank=True, null=True)  # Field name made lowercase.
    paymentdate = models.DateTimeField(db_column='PaymentDate', blank=True, null=True)  # Field name made lowercase.
    custsuffix = models.ForeignKey(Customer, models.DO_NOTHING, related_name="%(class)s_1607", db_column='CustSuffix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Remittance'
        unique_together = (('finame', 'fiaddress1', 'fiaddress2', 'fincity', 'finstate', 'finzip', 'fiphone', 'contractnumber', 'lineofbusiness', 'seriesname', 'planname'),)


class Stateregions(models.Model):
    custstate = models.CharField(db_column='CustState', primary_key=True, max_length=30)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StateRegions'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING, related_name="%(class)s_1634")
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING, related_name="%(class)s_1635")

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, related_name="%(class)s_1645")
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name="%(class)s_1673")
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING, related_name="%(class)s_1674")

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name="%(class)s_1684")
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING, related_name="%(class)s_1685")

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, related_name="%(class)s_1699", blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name="%(class)s_1700")

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
