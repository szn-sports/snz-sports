Parse.serverURL = 'https://parseapi.back4app.com';
Parse.initialize('N91bT7aVMOcfFP20VE0QI5wlhoUu38MI3jL66YDL', '9wV7QWg4VTRpL08Krnc5tnPu7XveXnH25TNBJmyV', 'OZ6ZC2R3iRxeRPxs6TpDUsJI9IQcqIb7tnQJ2TXA');

(async () => {
  const allObjects = Parse.Object.extend('allObjects');
  const query = new Parse.Query(allObjects);
  // You can also query by using a parameter of an object
  // query.equalTo('objectId', 'xKue915KBG');
  try {
    const results = await query.find();
    for (const object of results) {
      // Access the Parse Object attributes using the .GET method
      const pid = object.get('pid')
      console.log(pid);
    }
  } catch (error) {
    console.error('Error while fetching allObjects', error);
  }
})();
;