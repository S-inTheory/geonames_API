<h1> Выполненное тестовое задание для стажера на позицию «Аналитик (python)» </h1>



<h2> Instalation </h2>

Please make sure the files is unpacked under a Web-accessible directory. You shall see the following files and directories:

<pre>
<code>
  geonames_API/        main folder of project
  convertors           folder with scripts that convert *.txt to *.json,
                       and *.json to database file 
  gAPI                 our application folder
  geonames_API         folder with our project files
  static               folder with static files
  .flake8              flake8 config file
  db.sqlite3           database file
  manage.py            Django's command-line utility
                       for administrative tasks
  readme.md            this file
  requirements.txt     requirements checker
  RU.txt               file with data for working with
  script.py            executable file for this project
</code>
</pre>

How methods works

<pre>
<code>
  /geoname-list/id/                                             First method gets geonameid instead of "id" in URL
                                                                and return detail information about city
                                                    
  /geoname-list/?page="pagenumber"&page_size="pagesize"         Second method get number of page
                                                                instead of "pagenumber" and number
                                                                of elements on page instead of "pagesize"
                                                                and return needed page with requested quantity
                                                                of cities in it
                                                         
  /geonames/search/                                             Third method gets comma-separated list of
                                                                two names of cities in Russian instead of "search" and 
                                                                returns detailed information about two cities, which city
                                                                northern, about equality of timezones, and timezones 
                                                                difference in hours
</code>
</pre>


<h2> Quick start </h2>

On command line in virtual environment, type in the following commands:

<pre>
<code>
  $ python script.py  
</code>
</pre>