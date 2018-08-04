# Bokujo REST-Api Server

## API Endpoints


### Updating database tables and columns in local and Heroku environment
1.  Run `python manage.py db migrate` locally when a new table or column is added
2. Run `python manage.py db upgrade` to commit changes to the database
3. Deploy to Heroku
4.  Run `heroku run db upgrade`
