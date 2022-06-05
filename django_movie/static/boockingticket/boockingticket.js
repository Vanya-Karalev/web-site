$("#date").html(localStorage.getItem('MovieDate'));
$("#time").html(localStorage.getItem('MovieTime'));
// $("#name").html(localStorage.getItem('MovieName'));
// localStorage.clear();
const mycontainer = document.querySelector('.mycontainer');
const seats = document.querySelectorAll('.row .seat:not(occupied)');
const count = document.getElementById('count');
const total = document.getElementById('total');
const movieSelect = document.getElementById('movie');

populateUI();

let ticketPrice = 10; // + will convert it into number

// Save selected movie index and price
function setMovieData(movieIndex, moviePrice) {
  localStorage.setItem('selectedMovieIndex', movieIndex);
  localStorage.setItem('selectedMoviePrice', moviePrice);
}

// Update total and count
function updateSelectedCount(e) {
  const selectedSeats = document.querySelectorAll('.row .seat.selected');

  const seatsIndex = [...selectedSeats].map(seat => {
    return [...seats].indexOf(seat);
  });
  // localStorage.setItem('selectedSeats', JSON.stringify(seatsIndex));

  console.log(seatsIndex);
  const selectedSeatsCount = selectedSeats.length;

  count.innerText = selectedSeatsCount.toString();
  total.textContent = (selectedSeatsCount * ticketPrice).toString() ;
  console.log(total);
}

// Get Data from localstorage and populate UI
function populateUI() {
  const selectedSeats = JSON.parse(localStorage.getItem('selectedSeats'));

  if (selectedSeats !== null && selectedSeats.length > 0) {
    seats.forEach((seat, index) => {
      if (selectedSeats.indexOf(index) > -1) {
        seat.classList.add('selected');
      }
    });
  }

  const selectedMovieIndex = localStorage.getItem('selectedMovieIndex');

  if (selectedMovieIndex !== null) {
    movieSelect.selectedIndex = selectedMovieIndex;
  }
}

// Movie Select event
movieSelect.addEventListener('change', e => {
  ticketPrice = +e.target.value;
  setMovieData(e.target.selectedIndex, e.target.value);
  updateSelectedCount();
  getTakenSeats();
});

// Seat click event
mycontainer.addEventListener('click', e => {
  if (
    e.target.classList.contains('seat') &&
    !e.target.classList.contains('occupied')
  ) {
    console.log(e.target);
    e.target.classList.toggle('selected');
  }

   // select a seat and turn it blue

  updateSelectedCount();
});

//Initial count and total set
updateSelectedCount();
