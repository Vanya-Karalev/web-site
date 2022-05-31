console.log('hello world')

const url = window.location.href
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const resultsBox = document.getElementById('results-box')

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
console.log(csrf)

const sendSearchData = (movie) => {
    $.ajax({
        type: 'POST',
        url: 'search_results/',
        data: {
            'csrfmiddlewaretoken': csrf,
            'movie': movie,
        },
        success: (res)=> {
            console.log(res.data)
            const data = res.data
            if (Array.isArray(data)){
                console.log('we have an array')
                resultsBox.innerHTML = ""
                data.forEach(movie=>{
                    resultsBox.innerHTML += `
                         <a href="${url}${'movieinfo'}${movie.id}" class="item">
                             <div class="row mt-2 mb-2">
                                 <div class="movieImg">
                                     <img style="height: 200px;" src="${movie.poster}">
                                 </div>
                                 <div class="movieText">
                                     <h5>${movie.title}</h5>
                                     <p class="text-muted"></p>
                                 </div>
                             </div>
                             <hr class="horizontalLine">
                         </a>`
                })
            } else{
                if (searchInput.value.length > 0){
                    resultsBox.innerHTML = `<b>${data}</b>`
                } else {
                    resultsBox.classList.add('not-visible')
                }
            }
        },
        error: (err)=> {
            console.log(err)
        }
    })
}

searchInput.addEventListener('keyup', e=>{
    console.log(e.target.value)

    if (resultsBox.classList.contains('not-visible')){
        resultsBox.classList.remove('not-visible')
    }

    sendSearchData(e.target.value)
})