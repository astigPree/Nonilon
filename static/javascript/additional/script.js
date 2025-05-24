
// window.addEventListener('DOMContentLoaded', function() {
    
//     const projectBody = document.getElementById('additional-content')
//     projectBody.style.opacity = 1;

//     const submit_button = document.getElementById('submit-testimonial');
//     submit_button.disabled = false;



//     const testimonials_list = document.getElementById('list-of-testimonials');

    




//     submit_button.addEventListener('click',  async function(event) { 

//             event.preventDefault();
            
//             if (submit_button.disabled) {
//                 return;
//             }

//             submit_button.disabled = true;

//             // Checking data
//             const name = document.getElementById('client-name-form').value
//             const testimony = document.getElementById('testimony').value
//             const key = document.getElementById('client-key').value
//             const rating = document.getElementById('current-rate').getAttribute('data')


//             const csrfToken = document.querySelector('#csrf-token').value;  

//             if (!name || name.length > 15) {
//                 toastAnimation('Please enter a valid name!');
//                 submit_button.disabled = false;
//                 return;
//             }

//             if (!testimony || testimony.length > 335) {
//                 toastAnimation('Please enter a valid testimony!');
//                 submit_button.disabled = false;
//                 return;
//             }

//             if (!key || key.length > 15) {
//                 toastAnimation('Please enter a valid key!');
//                 submit_button.disabled = false;
//                 return;
//             }

//             if (!rating || rating < 1 || rating > 5) {
//                 toastAnimation('Please select a valid rating!');
//                 submit_button.disabled = false;
//                 return;
//             }

            
//             const formData = new FormData();
//             formData.append('name', name);
//             formData.append('testimony', testimony);
//             formData.append('client_code', key);
//             formData.append('rating', rating);
            
//             try{

//                 const response = await fetch(submit_button.getAttribute('location'), {
//                     method: 'POST',
//                     headers: { 
//                         'X-Requested-With': 'XMLHttpRequest',
//                         'X-CSRFToken': csrfToken
//                     },
//                     body: formData
//                 });
                    
//                 const data = await response.json();
    
//                 if (response.ok) {
//                     window.location.reload();
//                     submit_button.disabled = false;
//                 } else {
//                     toastAnimation(data.message);
//                     submit_button.disabled = false;
//                 }

//             } catch (error) {
//                 submit_button.disabled = false;
//             }
//             submit_button.disabled = false;
            
//         }
    
//     );
    


// });