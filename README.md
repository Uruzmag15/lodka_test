
##### The application requires:
<ul>
    <li>Docker: https://docs.docker.com/install/linux/docker-ce/ubuntu/</li>
    <li>docker-compose: https://docs.docker.com/compose/install/</li>
</ul>

##### Prepare to run:
<ol>
    <li>Install "Docker" and "docker-compose"</li>
    <li>"git clone https://github.com/Uruzmag15/lodka_test.git"</li>
    <li>"cd lodka_test/"</li>
    <li>"docker-compose run web python /code/manage.py migrate --noinput"</li>
    <li>"docker-compose run web python /code/manage.py createsuperuser"</li>
</ol>

##### To run:
<ul>
    <li>"docker-compose up -d --build"</li>
    <li>Open in browser: "0.0.0.0:8000/api/v1/categories/"</li>
</ul>

##### To shutdown:
<ul>
    <li>"docker-compose down"</li>
</ul>

If you have an error: 
"
ERROR: Couldn't connect to Docker daemon at http+docker://localhost - is it running?
If it's at a non-standard location, specify the URL with the DOCKER_HOST environment variable." 

Try all docker commands with "sudo".
