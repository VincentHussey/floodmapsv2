createuser -U postgres -d -l -R -S -P flood 
createdb -U postgres -E UTF8 -O flood floodmaps
createlang -U postgres plpgsql floodmaps
psql -U postgres -d floodmaps -f /usr/share/postgresql/8.4/contrib/postgis-1.5/postgis.sql
psql -U postgres -d floodmaps -f /usr/share/postgresql/8.4/contrib/postgis-1.5/spatial_ref_sys.sql
psql -U postgres -d floodmaps -c "alter table spatial_ref_sys owner to flood"
psql -U postgres -d floodmaps -c "alter table geometry_columns owner to flood"
psql -U postgres -d floodmaps -c "alter table geography_columns owner to flood"

