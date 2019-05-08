$(document).ready(function() {
    $('#search-btn').on('click',function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/candies?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="well candy">
                            <a href="/candies/${d.id}">
                                <img class="candy-img" src="${d.firstImage}" />
                                <h4>${d.name}</h4>
                                <p>${d.description}</p>
                            </a>
                        </div>`
                });
                $('.candies').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function(xhr, status, error) {
                //TODO: show toastr
                console.error(error);
            }
        })
    });
});