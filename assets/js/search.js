//supremeproject/assets/search.js
//define the search criteria by array, it would be iterated in showSelected function
const criteria = ["ID", "Date"];

//create the criteria button for selecting column type for searching
const searchby = document.querySelector('#searchby');
searchby.innerHTML = criteria.map((criterion) => `<input type="radio" name="search_criteria" value="${criterion}" id="${criterion}" >
<label for="${criterion}">${criterion}</label>`).join(' ');

//declare the variable for displaying the button by iterating the element name
const radioButtons = document.querySelectorAll('input[name=search_criteria]')
for (const radioButton of radioButtons) {
  radioButton.addEventListener('change', showSelected)
}

//customized function for displaying the particular column type
function showSelected(e) {
  console.log(e);
  //show the id finder column
  if(this.value == "ID") {
    document.querySelector('#search').innerHTML = `<form action="specified_result.php" method="get">
    <input class="input_form" type="number" name="id" placeholder="Find by ID...">
    </form>`;
  }

  //display the date finder column
  if(this.value == "Date") {
    document.querySelector('#search').innerHTML = `<form action="specified_date.php" method="get">
    <input class="input_form" type="text" name="date" placeholder="Find by date...">
    </form>`;
  }
}
