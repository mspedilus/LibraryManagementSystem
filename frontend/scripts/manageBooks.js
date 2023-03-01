//Autofills table with books in the database

function deleteItem(tag) {
    var tr = tag.closest('tr');
    console.log(tr)
    var willDelete = confirm(`Are you sure you want to delete the book: ${tr.dataset.name}?`);
    if (willDelete) {
        callApi("POST", deleteBookUrl, { book_id: tr.dataset.id });
    }
}

function editItem(tag) {
    var data = JSON.parse(tag.closest("tr").dataset.data)
    document.getElementById("edit_isbn").value = data.ISBN
    document.getElementById("edit_title").value = data.book_title
    document.getElementById("edit_author").value = data.author_name
    document.getElementById("edit_publisher").value = data.publisher
    document.getElementById("edit_desc").value = data.description
    document.getElementById("edit_category").value = data.category
    document.getElementById("edit_price").value = data.price
    document.getElementById("edit_qty").value = data.quantity
}

$(document).ready(() =>{
    //Json data by api call for order table
    $.get(getAllBooksUrl, (response) => {
        if(response) {
            var table = '';
            $("#bookTotal").text("Total: " + response.length || 0)
            $.each(response, (index, book) => {
                 table += `<tr data-id="${book.book_id}" data-name="${book.book_title}" data-data=${JSON.stringify(book)}> ` +
                    '<td>'+ book.ISBN +'</td>'+
                    '<td>'+ book.book_title +'</td>'+
                    '<td>'+ book.author_name +'</td>'+
                    '<td>'+ book.description +'</td>'+
                    '<td>'+ book.publisher +'</td>' +
                    '<td>'+ book.category +'</td>'+
                    '<td>$'+ book.price +'</td>'+
                    '<td>'+ book.quantity +'</td>' +
                    '<td><button onclick="editItem(this)" type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#editModal">' + 
                    '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="20" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">' +
                    '<path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>' + 
                    '<path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>' +
                    '</svg></button>' +
                    '<button type="button" onclick="deleteItem(this)" class="btn btn-danger delete">x</button></td></tr>';
            });
            $("table").find('tbody').html(table);
        }
    });


    
    $(document).on("click", ".save", () => {
        var form = $("#bookForm").serializeArray();
        var data = { 
            "ISBN": form[0].value, 
            "book_title": form[1].value, 
            "author_name": form[2].value, 
            "description": form[3].value,
            "publisher": form[4].value, 
            "category": form[5].value, 
            "price": form[6].value, 
            "quantity": form[7].value, 
        }
        callApi("POST", insertBookUrl, {"data": JSON.stringify(data)}) 
    })

});


