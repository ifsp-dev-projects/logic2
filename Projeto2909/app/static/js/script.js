document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.check-tarefa').forEach(checkbox => {

        checkbox.addEventListener('change', function() {
            const tarefaId = this.dataset.tarefaId
            const textoTarefa = document.getElementById(`texto-tarefa-${tarefaId}`);

            fetch(`/tarefa/concluir/${tarefaID}`), {
                method: 'POST'
            }
            .then(response => response.json())
            .then(data =>{
                if (data.status === 'sucesso') {
                    textoTarefa.classList.toggle('concluida', data.concluida)
                }
            })
            .catch(error => console.error('Houve um erro na requisição AJAX:', error));
        });
    });
});