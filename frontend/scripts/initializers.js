// Define your api here
var getAllBooksUrl = 'http://127.0.0.1:5000/getAllBooks'
var insertBookUrl = 'http://127.0.0.1:5000/insertBook'
var deleteBookUrl = 'http://127.0.0.1:5000/deleteBook'
var editBookUrl = 'http://127.0.0.1:5000/editBook'


function callApi(method, url, data) {
    $.ajax({
        method: method,
        url: url,
        data: data
    }).done(() => {
        window.location.reload();
    });
}

