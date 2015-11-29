df = load 's3n://<bucket_1>/<bucket_2>' using PigStorage(',') as ( bidid:chararray, traffictype:chararray, publisherid:chararray, appsiteid:chararray, appsitecategory:chararray, position:chararray, bidfloor:chararray, timestamp:chararray, age:chararray, gender:chararray, os:chararray, osvrsn:chararray, model:chararray, manufacturer:chararray, carrier:chararray, devicetype:chararray, deviceid:chararray, deviceip:chararray, country:chararray, lat:chararray, long:chararray, zipcode:chararray, geotype:chararray, campaignid:chararray, creativeid:chararray, Creativetype:chararray, creativecategory:chararray, exchangebid:chararray, outcome:chararray);

dfa = foreach df generate deviceid,deviceip,outcome,((outcome matches 'c')?1:0) as click,((outcome matches 'w')?1:0) as impression;

df_grp = group dfa by (deviceid);

result_count 	= 	foreach df_grp {
                           distinct_ips = DISTINCT dfa.deviceip;
						   generate
						      flatten(group),
							  COUNT(distinct_ips) as dist_ips,
							  SUM(dfa.click) as clicks,
							  SUM(dfa.impression) as impressions;
			};

resdf = order result_count by impressions desc;

resdf_ = limit resdf 100;
store resdf_ into 's3n://<output_dir>/<output>/' using PigStorage('\t');
