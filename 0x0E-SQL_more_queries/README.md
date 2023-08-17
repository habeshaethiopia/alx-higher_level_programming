<h1 class="gap">0x0E. SQL - More queries </h1>
<div class="panel-body">
    <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/66988091.jpg" alt="" loading="lazy" style=""></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/RniBKj48bnIN8xpXhGl1yA" title="How To Create a New User and Grant Permissions in MySQL" target="_blank">How To Create a New User and Grant Permissions in MySQL</a> </li>
<li><a href="/rltoken/FIiEIvA6IN_hSKM5TvgyxQ" title="How To Use MySQL GRANT Statement To Grant Privileges To a User" target="_blank">How To Use MySQL GRANT Statement To Grant Privileges To a User</a> </li>
<li><a href="/rltoken/LrovGa6N-OE2ID_tpWZRaQ" title="MySQL constraints" target="_blank">MySQL constraints</a> </li>
<li><a href="/rltoken/kR71h5zjkPtx4kBoVf7q0g" title="SQL technique: subqueries" target="_blank">SQL technique: subqueries</a> </li>
<li><a href="/rltoken/rNMJeQ1jbNTCljbvCSjf6w" title="Basic query operation: the join" target="_blank">Basic query operation: the join</a> </li>
<li><a href="/rltoken/HhZ6TJ1q5S0aR4lhfpKdOQ" title="SQL technique: multiple joins and the distinct keyword" target="_blank">SQL technique: multiple joins and the distinct keyword</a> </li>
<li><a href="/rltoken/T6FZUQdsMzr8hgNInBzudA" title="SQL technique: join types" target="_blank">SQL technique: join types</a> </li>
<li><a href="/rltoken/Nd-sdM8QUpf0YKIlXzVv4w" title="SQL technique: union and minus" target="_blank">SQL technique: union and minus</a> </li>
<li><a href="/rltoken/iSNyinU6SPWTGDUWMmcRkg" title="MySQL Cheat Sheet" target="_blank">MySQL Cheat Sheet</a> </li>
<li><a href="/rltoken/-plhBsra0N7BOuFoEg--zg" title="The Seven Types of SQL Joins" target="_blank">The Seven Types of SQL Joins</a> </li>
<li><a href="/rltoken/I4Lws_eQrIrNTbkZvvk-oQ" title="MySQL Tutorial" target="_blank">MySQL Tutorial</a> </li>
<li><a href="/rltoken/051eAEP_rePBU7jeh879GA" title="SQL Style Guide" target="_blank">SQL Style Guide</a> </li>
<li><a href="/rltoken/YavbYiraYFr8oTukT_N6eQ" title="MySQL 8.0 SQL Statement Syntax" target="_blank">MySQL 8.0 SQL Statement Syntax</a> </li>
</ul>

<p>Extra resources around relational database model design:</p>

<ul>
<li><a href="/rltoken/EWLRPeqr5sQ9AqfoG_KXxw" title="Design" target="_blank">Design</a></li>
<li><a href="/rltoken/mqBhYoSYbhH5ZZrhDcY0kA" title="Normalization" target="_blank">Normalization</a></li>
<li><a href="/rltoken/R0exkJmf-2ddKjGfa8D0dA" title="ER Modeling" target="_blank">ER Modeling</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/0qci3VdIVdKJXldEZ6zAjA" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>How to create a new MySQL user</li>
<li>How to manage privileges for a user to a database or table</li>
<li>What’s a <code>PRIMARY KEY</code></li>
<li>What’s a <code>FOREIGN KEY</code></li>
<li>How to use <code>NOT NULL</code> and <code>UNIQUE</code> constraints</li>
<li>How to retrieve datas from multiple tables in one request</li>
<li>What are subqueries</li>
<li>What are <code>JOIN</code> and <code>UNION</code></li>
</ul>

<h3>Copyright - Plagiarism</h3>

<ul>
<li>You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.</li>
<li>You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work. </li>
<li>You are not allowed to publish any content of this project.</li>
<li>Any form of plagiarism is strictly forbidden and will result in removal from the program.</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be executed on Ubuntu 20.04 LTS using <code>MySQL 8.0</code> (version 8.0.25)</li>
<li>All your files should end with a new line</li>
<li>All your SQL queries should have a comment just before (i.e. syntax above)</li>
<li>All your files should start by a comment describing the task</li>
<li>All SQL keywords should be in uppercase (<code>SELECT</code>, <code>WHERE</code>…)</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h2>More Info</h2>

<h3>Comments for your SQL file:</h3>

<pre><code>$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
</code></pre>

<h3>Install MySQL 8.0 on Ubuntu 20.04 LTS</h3>

<pre><code>$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
</code></pre>

<p>Connect to your MySQL server:</p>

<pre><code>$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql&gt;
mysql&gt; quit
Bye
$
</code></pre>

<h3>Use “container-on-demand” to run MySQL</h3>

<p><strong>In the container, credentials are <code>root/root</code></strong></p>

<ul>
<li>Ask for container <code>Ubuntu 20.04</code></li>
<li>Connect via SSH</li>
<li>OR connect via the Web terminal</li>
<li>In the container, you should start MySQL before playing with it:</li>
</ul>

<pre><code>$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
</code></pre>

<p><strong>In the container, credentials are <code>root/root</code></strong></p>

<h3>How to import a SQL dump</h3>

<pre><code>$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
</code></pre>

<p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/bc2575fee3303b731031.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230816%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20230816T205002Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=45b44b0b843027f68e743f61a1a1095611e03c6c1962be3c2743ba1e2cefefb2" alt="" loading="lazy" style=""></p>

  </div>