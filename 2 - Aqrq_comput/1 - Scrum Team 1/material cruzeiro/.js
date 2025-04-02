// Description: function to get the current date
function getCurrentDate() {
  var d = new Date();
  var day = d.getDate();
  var month = d.getMonth() + 1;
  var year = d.getFullYear();
  var hour = d.getHours();
  var minute = d.getMinutes();
  var second = d.getSeconds();
  var date =
    year + "-" + month + "-" + day + " " + hour + ":" + minute + ":" + second;
  return date;
}
