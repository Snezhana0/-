const DATA =[
    {
        question:'Сколько основных фильмов про Шрека?',
        answers:[
            {
                id:'1',
                value:'2',
                correct: false,
            },
            {
                id:'2',
                value: '5',
                correct: false,
            },
            {
                id:'3',
                value:'4',
                correct: true
            }


        ]
    },
    {
        question: 'Кто главный злодей во втором фильме?',
        answers: [
            {
                id: '4',
                value: 'Пряня',
                correct: false,
            },
            {
                id: '5',
                value: 'Лорд Фаркуад',
                correct: false,
            },
            {
                id: '6',
                value: 'Фея Крёстная',
                correct: true,
            },

        ]

    },
    {
        question: 'Кто озвучивает в оригинале Кота в сапогах?',
        answers: [
            {
                id: '7',
                value: 'Антонио Бандерас',
                correct: true,
            },
            {
                id: '8',
                value: 'Джонни Депп',
                correct: false,
            },
            {
                id: '9',
                value: 'Кот',
                correct: false,
            },

        ]

    },
    {
        question: 'Чей трек играет в начале первого фильма?',
        answers: [
            {
                id: '10',
                value: 'Bloodhound Gang',
                correct: false,
            },
            {
                id: '11',
                value: 'Smash Mouth',
                correct: true,
            },
            {
                id: '12',
                value: 'Fatboy Slim',
                correct: false,
            },

        ]

    },

];


let localResults = {};


const quiz = document.getElementById('quiz');
const questions = document.getElementById('questions');
const indicator = document.getElementById('indicator');
const  results = document.getElementById('results');
const btNext= document.getElementById('btn-next');
const  btRestart  = document.getElementById('btn-restart');

const renderQuestions=(index)=> {
    renderIndicator(index + 1);

    questions.dataset.currentStep = index;

    const renderAnswers = () => DATA[index].answers
        .map((answer) =>  `
           <li>
              <label>
                  <input class="answer-input" type="radio" name=${index} value=${answer.id}>
                   ${answer.value}
              </label>
           </li> 
        `)
        .join('');
    questions.innerHTML=`
        <div class="quiz-questions-item">
            <div class="quiz-questions-item_question">${DATA[index].question}</div>
            <ul class="quiz-question-item_answers">${renderAnswers()}</ul>
        </div>
    `;
};


const renderResults = () => {
    let content = '';

    const getClassname = (answer, questionIndex) =>{
        let classname = '';

        if(!answer.correct && answer.id === localResults[questionIndex]){
            classname = 'answer--invalid';
        }
        else if (answer.correct){
            classname = 'answer-valid';
        }
        return classname;
    }
    const getAnswers = (questionIndex) => DATA[questionIndex].answers
        .map((answer) => `<li class=${getClassname(answer, questionIndex)}>${answer.value}</li>`)
        .join('');

    DATA.forEach((question, index) => {
        content += `
            <div class="quiz-results-item">
                <div class="quiz-results-item_question" >${question.question}</div>
                <ul class="quiz-results-item_answers">${getAnswers(index)}</ul>
            </div>
        `;

    });

    results.innerHTML = content;
};
const renderIndicator=(currentStep)=>{
    indicator.innerHTML=`${currentStep}/${DATA.length}`;
};

quiz.addEventListener('change', (event)=>{
    if(event.target.classList.contains('answer-input')){
        localResults[event.target.name] = event.target.value;
        btNext.disabled = false;
        console.log('localResults');
    }
});

quiz.addEventListener('click',(event)=>{
    if(event.target.classList.contains('btn-next')){
        const nextQuestionIndex = Number(questions.dataset.currentStep) + 1;

        if (DATA.length === nextQuestionIndex){
            questions.classList.add('questions--hidden');
            indicator.classList.add('indicator--hidden');
            results.classList.add('results--visible');
            btNext.classList.add('btn-next--hidden');
            btRestart.classList.add('btn-restart--visible');
            renderResults();
        }
        else{
            renderQuestions(nextQuestionIndex);
        }
        btNext.disabled = true;
    }

    if(event.target.classList.contains('btn-restart')){
        localResults={};
        results.innerHTML='';

        questions.classList.remove('questions--hidden');
        indicator.classList.remove('indicator--hidden');
        results.classList.remove('results--visible');
        btNext.classList.remove('btn-next--hidden');
        btRestart.classList.remove('btn-restart--visible');

        renderQuestions(0);
    }
});

renderQuestions(0);