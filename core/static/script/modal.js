$(document).ready(function () {
    $('#task-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const taskID = button.data('source') // Extract info from data-* attributes
        const content = button.data('content') // Extract info from data-* attributes
        const date = button.data('date')

        const modal = $(this)
        if (taskID === 'New Task') {
            modal.find('.modal-title').text(taskID)
            $('#task-form-display').removeAttr('taskID')
        } else {
            modal.find('.modal-title').text('Edit Task ' + taskID)
            $('#task-form-display').attr('taskID', taskID)
        }

        if (content) {
            modal.find('.task-title').val(content);
            modal.find('.task-date').val(date)
        } else {
            modal.find('.form-control').val('');
        }
    })


    $('#edit-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const taskID = button.data('source') // Extract info from data-* attributes
        const content = button.data('content') // Extract info from data-* attributes
        const date = button.data('date')
        console.log(taskID)
        console.log(content)
        console.log(date)
        $.ajax({
            type: 'GET',
            url: '/edit/' + taskID,
            success: function (res) {
                console.log(res.response)
            }
        })
        const modal = $(this)
        modal.find('.modal-title').text('Edit Task ' + taskID)
        console.log(document.getElementsByName("ind"))
    })

    $('.remove').click(function () {
        const remove = $(this)
        $.ajax({
            type: 'POST',
            url: '/delete/' + remove.data('source'),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.state').click(function () {
        const state = $(this)
        const tID = state.data('source')
        let new_state = "To Do"
        if (state.text() === "In Progress") {
            new_state = "Complete"
        } else if (state.text() === "Complete") {
            $.ajax({
            type: 'POST',
            url: '/delete/' + tID,
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }});
        } else if (state.text() === "To Do") {
            new_state = "In Progress"
        }

        $.ajax({
            type: 'POST',
            url: '/progress/' + tID,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'status': new_state
            }),
            success: function (res) {
                console.log(res)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

});