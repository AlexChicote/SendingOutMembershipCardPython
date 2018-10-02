# SendingOutMembershipCardPython
Using a list of members, a png file, python and some libraries (mainly reportlab and MIME, we send out through email the membership cards to the members

This is a small project that I did to help out my soccer fan club to develop a system to send a provisional membership card once the members sign up. It is obviously a project that could be more developed but that was able to solve the problem that they fan club was facing. Hopefully, it might help somebody else. Needless to say: any feedback is welcome 

Summary of steps:

  1. Creating the dataframe. I obtained all data from a xml file from where I generated the list of members> I execute the       file at the beguinning.
  2. Once the members df is created, using a for loop I generated he membership and send it out through repportlab and MIME.
  3. In order to use it with updates. I create a file where I store the ID sent so only the new ones are sent out next time I   use the script

