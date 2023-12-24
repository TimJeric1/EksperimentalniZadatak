## Prerequesites
Python
Docker


## Commands to run one by one (tested in fedora 39 linux):

### Run inside simple_db folder:


``` 
docker-compose up --build -d 
pip install --no-cache-dir faker mysql-connector-python matplotlib
```

if you get this error: Error starting userland proxy: listen tcp4 0.0.0.0:3306: bind: address already in use
then you need to run this command on the port of the error 
```
sudo netstat -nlpt |grep 3306
```
and remove the service that is shown
```
sudo service <service-name> stop
```
or
```
sudo kill <pid>
```

then generate data:
```
python generate_data_simple.py 
```

if you receive this error:
"Lost connection to MySQL server at 'reading initial communication packet' fails"
wait 5 seconds and just rerun the last command

in second terminal run:
```
python flaskapp.py
```
After that (it can take about a minute)
```
python measure_and_plot.py
```

When you are done with measuring simple_db:
```
docker-compose down
```
and ctrl-c in the flaskapp.py terminal to terminate the backend server

### Run inside replicated_2_db folder:
```
./build.sh
pip install --no-cache-dir faker mysql-connector-python matplotlib
python generate_data_replicated.py
```

if you get permission denied just:
```
chmod +x <the_file_name>
```

in some other terminal run
```
python flaskapp.py
```
After that wait a few seconds for slave to catch up with data:
you can use to check if slave caught up:
```
docker exec -it mysql_slave mysql -uroot -p111
use mydb
select * from users;
exit
```
after that benchmark the performance with:
```
python measure_and_plot.py 
```

When you are done with measuring replicated_2_db:
```
docker-compose down
sudo rm -rf ./master/data/*
sudo rm -rf ./slave/data/*
ctrl-c in the flaskapp.py terminal to terminate the backend server
```
