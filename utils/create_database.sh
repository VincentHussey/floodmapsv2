createuser -U postgres -d -l -R -S -P flood 
createdb -U postgres -E UTF8 -O flood floodmaps
createlang -U postgres plpgsql floodmaps
psql -U postgres -d floodmaps -f /usr/share/pgsql/contrib/postgis.sql -d floodmaps
psql -U postgres -d floodmaps -f /usr/share/pgsql/contrib/spatial_ref_sys.sql -d floodmaps
