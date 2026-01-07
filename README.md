# home-assessment
Short questions
What assumptions did you make?
I assumed that events without id's and wrong timestamp should be skipped. Duplicate events should br considered as one by normalizing, here i use set to store clean events that prevent duplicate objects.Purchase action contains amount and converted it in to integer.And finally the cleaned actions and amount of purchase should be counted.
 * What edge cases did you notice?
   The edge cases are as follow
   1.Missind ID's
   2.invalid Timestamps
   3.Not single format of timestamps
   4 Duploicate enteries of same events
 * What would you improve if this were production code?
    i will improve following things if this were a production code
   1.i will add data checks so that we avoid ignoring bad rows
   2 give error msg when enter the data so that we can't lose the information
   3.i will break the analysis and cleaning module differently so the data organized properly and easy to maintain.
   ----------------------------------------------------------------------------------
Your background is more inclined toward AI and Computer Vision, while most work at DevNodes is focused on backend and product engineering.
If you were to join us and spend the next year mostly on non-AI work, how would you look at this decision in terms of your long-term growth?

Thank you for bringing up the interesting question. I've given it some thought and realized that I would like to incorporate TypeScript into my full-stack goals with this web-app development opportunity.
I believe adding TypeScript will allow me to stand on much stronger ground in a few years with my full-stack selection. I am here to learn and grow under your leadership, and I am committed to making the most of this opportunity.Please let me know if there is anything you would recommend, based on your experience, that could help me shape my career more appropriately.
