import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const response = [];
  const promiseSignUp = signUpUser(firstName, lastName);
  const promiseUpload = uploadPhoto(fileName);

  return Promise.allSettled([promiseSignUp, promiseUpload])
    .then((results) => {
      results.forEach((result) => {
        const value =
          typeof result.value === 'undefined'
            ? result.reason.toString()
            : result.value;
        response.push({ status: result.status, value: value });
      });
    })
    .finally(() => response);
}
