echo "intra Ski7"
process_output.py -f stat.out -t Distance | awk '(NF==0){print "#"};(NF!=0){print}'| tr -s ":" " " | tr -s "_" " " |  tr -s "-" " " | awk 'BEGIN{ns=0;n=0};($7=="Ski7"&&$9=="Ski7"){if($NF<=35){ns=ns+1;n=n+1};if($NF>35){n=n+1}};($NF=="#"){print ns/n,n,ns;ns=0;n=0}' | awk '{nsatcrossl=nsatcrossl+$3;n=n+1;print $2};END{print nsatcrossl/n}'
echo "inter Ski7"
process_output.py -f stat.out -t Distance | awk '(NF==0){print "#"};(NF!=0){print}'| tr -s ":" " " | tr -s "_" " " |  tr -s "-" " " | awk 'BEGIN{ns=0;n=0};(($7=="Ski7"&&$9!="Ski7")||($7!="Ski7"&&$9=="Ski7")){if($NF<=35){ns=ns+1;n=n+1};if($NF>35){n=n+1}};($NF=="#"){print ns/n,n,ns;ns=0;n=0}' | awk '{nsatcrossl=nsatcrossl+$3;n=n+1; print $2};END{print nsatcrossl/n}'

