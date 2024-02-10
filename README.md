a group generator i created as internal VP of [Cal Hacks](https://www.calhacks.io/) to create better MEH* groups. randomly pairs people based on mbti compatibility, team, active status, and other factors to encourage people who don’t normally interact (but have a high possibility of vibing) to hang out :)

# details
1. to use, export google sheets as json (you will need to add this [script](https://thenewstack.io/how-to-convert-google-spreadsheet-to-json-formatted-text/)). my columns were name, status, team, mbti, and paired (people that have alr been matched), but you can easily add more features.
2. the generator will randomly pick a person based on the following:\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i. haven’t been grouped before\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ii. preferably people in different teams (although it's ok to pair people together with the same teams if it runs out of pairings)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iii. preferably people with compatible* mbtis (i created a simplified compatibility table based on the [myers briggs type compatibility chart](https://www.dreamsaroundtheworld.com/wp-content/uploads/2017/01/Myers_Briggs_Type_Compatibility_Chart.pdf), where ”compatible” = dark green/blue)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iv. preferably people with different statuses (active, inactive, new member)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;v. once a person is paired with someone for that week, they cannot be paired with someone else

you can easily adjust this to match people with "incompatible" mbti types as well by changing a bool :)

---
*mandatory enforced hangouts
