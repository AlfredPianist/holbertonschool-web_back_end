import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(
  firstName,
  lastName,
  fileName,
) {
  const response = [];

  await signUpUser(firstName, lastName)
    .then(async (body) => {
      response.push({ status: 'fulfilled', value: body });
      await uploadPhoto(fileName);
    })
    .catch((error) => {
      response.push({ status: 'rejected', error: error.toString() });
    });
  return response;
}
