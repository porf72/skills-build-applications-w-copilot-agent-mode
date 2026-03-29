use octofit_db;

print('Collections:');
printjson(db.getCollectionNames());

const collections = ['users', 'teams', 'activities', 'leaderboard', 'workouts'];
collections.forEach(function(coll) {
  print('\nSample from ' + coll + ':');
  printjson(db[coll].findOne());
});
