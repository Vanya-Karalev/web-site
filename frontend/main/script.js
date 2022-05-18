const panels = document.querySelectorAll('.panel');

panels.forEach(panel => {
  panel.addEventListener('click', () => {
    removeActiveClasses();
    panel.classList.add('active');
  })
})

function removeActiveClasses() {
  panels.forEach(panel => {
    panel.classList.remove('active');
  })
}
// $("#image").css("background","url(https://yc.cldmlk.com/wmezace6a8ycqfbe2gjcg9vn0m/1648694165329_Poster.jpg) center / cover no-repeat");