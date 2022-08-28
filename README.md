# dbs_final_project
Author: Caglar Dogan
cd2647  N18970424

This program is designed to be run with python3.

Moreover, the 'ODBC Driver 18 for SQL Server' is required for the connections to Azure SQL Server.
Please see the following website on the directions to run this:

https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16


The crucial Django/Azure specific dependencies for this program are:

Django==4.0.7
django-mssql-backend==2.8.1
django-storages==1.13.1
mssql-django==1.1.3
azure-core==1.25.0
azure-storage-blob==12.13.1

Moreover, the following libraries should also be present for the ML models:
numpy
pandas
statistics
pickle
sklearn
matplotlib

In the requirements.txt, a much bigger set of dependencies is presented representing the environemnt in which I ran my tests. In case of any problem, please use an environment which satisfies the environment presented in requirements.txt to be sure that everything is stable.

In any event, you can reach out to me via the following e-mail address: cd2647@nyu.edu

