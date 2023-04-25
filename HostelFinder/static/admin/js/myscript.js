import {data} from "../../mydata"
(function (){
  function render(){
    console.log(data)
    const hostelsContainer = document.getElementById('hostels-container');

// Iterate through the data array using a for loop
for (let i = 0; i < data.length; i++) {
  // Get the current hostel from the data array
  const hostel = data[i];

  // Create a div element to hold the hostel details
  const hostelDiv = document.createElement('div');
  hostelDiv.className = 'hostel';

  // Create HTML elements to display the hostel name, price and rating
  const hostelName = document.createElement('h2');
  hostelName.innerText = hostel.Hostel_name;
  const hostelPrice = document.createElement('p');
  hostelPrice.innerText = `Price: Rs.${hostel.price}/month`;
  const hostelRating = document.createElement('p');
  hostelRating.innerText = `Rating: ${hostel.Rating}`;

  // Add the hostel name, price and rating elements to the hostel div
  hostelDiv.appendChild(hostelName);
  hostelDiv.appendChild(hostelPrice);
  hostelDiv.appendChild(hostelRating);

  // Create a Google Maps link to display the location of the hostel
  // const mapsLink = `https://www.google.com/maps/search/?api=1&query=${hostel.latitude},${hostel.longitude}`;
  // const mapsLinkElement = document.createElement('a');
  // mapsLinkElement.href = mapsLink;
  // mapsLinkElement.target = '_blank';
  // mapsLinkElement.innerText = 'View on Google Maps';

  // // Add the Google Maps link element to the hostel div
  // hostelDiv.appendChild(mapsLinkElement);

  // Add the hostel div to the hostels container
  hostelsContainer.appendChild(hostelDiv);}

    
  }
  document.getElementById('buttonSearch').addEventListener('onclick', render, true);
})();
