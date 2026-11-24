document.addEventListener('DOMContentLoaded', function() {
  // nav menu
  const menus = document.querySelectorAll('.side-menu');
  M.Sidenav.init(menus, {edge: 'right'});
});


// ===============================
// FORM ELEMENTS
// ===============================

const add_btn = document.querySelector('.add-btn');
const close_btn = document.querySelector('.close-btn');
const form = document.querySelector('.side-form');
const capture_div = document.querySelector('.capture-div');

const videoPlayer = document.querySelector('#player');
const canvasElement = document.querySelector('#canvas');
const captureButton = document.querySelector('#capture-btn');
const imagePicker = document.querySelector('#image-picker');
const imagePickerArea = document.querySelector('#pick-image');


// ===============================
// LOCATION ELEMENTS
// ===============================

const locationBtn = document.querySelector('#location-btn');
const locationLoader = document.querySelector('#location-loader');
const latInput = document.querySelector('#lat');
const lngInput = document.querySelector('#lng');

// NEW: GPS / PINCODE CHECKBOX
const useGpsCheckbox = document.querySelector('#use-gps');


// ===============================
// IMAGE ELEMENTS
// ===============================

const capture_btn = document.querySelector('.capture-btn');
const upload_btn = document.querySelector('.upload-btn');
const image_options = document.querySelector('.image-options');
const upload_section = document.querySelector('.upload-section');


// ===============================
// LOCATION BUTTON VISIBILITY
// ===============================

function updateLocationOption() {

  if (!useGpsCheckbox) {
      return;
  }

  if (useGpsCheckbox.checked) {

      // GPS selected
      if (locationBtn) {
          locationBtn.style.display = 'inline-block';
      }

  } else {

      // Pincode centroid selected
      if (locationBtn) {
          locationBtn.style.display = 'none';
      }

      if (locationLoader) {
          locationLoader.style.display = 'none';
      }

      // Clear any previously captured GPS
      if (latInput) {
          latInput.value = '';
      }

      if (lngInput) {
          lngInput.value = '';
      }
  }
}


// ===============================
// GPS / PINCODE CHECKBOX
// ===============================

if (useGpsCheckbox) {

  useGpsCheckbox.addEventListener('change', function() {

      updateLocationOption();

  });

  // Set initial state
  updateLocationOption();
}


// ===============================
// CAPTURE CURRENT GPS LOCATION
// ===============================

if (locationBtn) {

  locationBtn.addEventListener('click', () => {

      // GPS option must be selected
      if (useGpsCheckbox && !useGpsCheckbox.checked) {

          alert(
              'Please select "Use GPS coordinates" first.'
          );

          return;
      }


      // Browser does not support GPS
      if (!('geolocation' in navigator)) {

          alert(
              'Location is not supported by this browser. ' +
              'Pincode centroid will be used.'
          );

          if (latInput) {
              latInput.value = '';
          }

          if (lngInput) {
              lngInput.value = '';
          }

          return;
      }


      locationBtn.style.display = 'none';

      if (locationLoader) {
          locationLoader.style.display = 'block';
      }


      navigator.geolocation.getCurrentPosition(

          // ===============================
          // GPS SUCCESS
          // ===============================

          position => {

              const latitude = position.coords.latitude;
              const longitude = position.coords.longitude;


              if (latInput) {
                  latInput.value = latitude.toFixed(6);
              }

              if (lngInput) {
                  lngInput.value = longitude.toFixed(6);
              }


              if (locationLoader) {
                  locationLoader.style.display = 'none';
              }

              locationBtn.style.display = 'inline-block';

              locationBtn.textContent =
                  '📍 GPS Location Captured';


              console.log(
                  'GPS latitude:',
                  latitude
              );

              console.log(
                  'GPS longitude:',
                  longitude
              );
          },


          // ===============================
          // GPS ERROR
          // ===============================

          err => {

              if (locationLoader) {
                  locationLoader.style.display = 'none';
              }

              locationBtn.style.display = 'inline-block';


              if (latInput) {
                  latInput.value = '';
              }

              if (lngInput) {
                  lngInput.value = '';
              }


              alert(
                  'Current GPS location could not be captured. ' +
                  'Pincode centroid will be used instead.'
              );

          },


          {
              enableHighAccuracy: true,
              timeout: 7000,
              maximumAge: 0
          }

      );

  });

}


// ===============================
// CAMERA
// ===============================

const getCamera = async () => {

  let devices =
      await navigator.mediaDevices.enumerateDevices();

  let camaras =
      devices.filter(
          device => device.kind === 'videoinput'
      );

  if (!camaras.length) {
      throw new Error('No camera found');
  }

  let deviceID =
      camaras[camaras.length - 1].deviceId;

  return deviceID;
};


// ===============================
// INITIALIZE MEDIA
// ===============================

const initializeMedia = () => {

  if (!('mediaDevices' in navigator)) {

      navigator.mediaDevices = {};

      console.log(navigator);
  }


  if (!('getUserMedia' in navigator.mediaDevices)) {

      navigator.mediaDevices.getUserMedia =
          function(constraints) {

              let getUserMedia =
                  navigator.webkitGetUserMedia ||
                  navigator.mozGetUserMedia;

              if (!getUserMedia) {

                  return Promise.reject(
                      new Error(
                          'getUserMedia is not implemented!'
                      )
                  );
              }


              return new Promise(
                  (resolve, reject) => {

                      getUserMedia.call(
                          navigator,
                          constraints,
                          resolve,
                          reject
                      );

                  }
              );
          };
  }


  getCamera()
      .then(cID => {

          let streamConstraints = {
              video: {
                  deviceId: cID
              }
          };

          console.log(streamConstraints);


          navigator.mediaDevices
              .getUserMedia(streamConstraints)

              .then(function(stream) {

                  if (videoPlayer) {

                      videoPlayer.srcObject = stream;

                      videoPlayer.style.display =
                          'block';
                  }

              })

              .catch(function(err) {

                  if (imagePickerArea) {

                      imagePickerArea.style.display =
                          'block';
                  }

              });

      })

      .catch(function(err) {

          if (imagePickerArea) {

              imagePickerArea.style.display =
                  'block';
          }

      });
};


// ===============================
// IMAGE CAPTURE
// ===============================

let picture;


function dataURItoBlob(dataURI) {

  var byteString =
      atob(dataURI.split(',')[1]);

  var mimeString =
      dataURI
          .split(',')[0]
          .split(':')[1]
          .split(';')[0];

  var ab =
      new ArrayBuffer(byteString.length);

  var ia =
      new Uint8Array(ab);


  for (
      var i = 0;
      i < byteString.length;
      i++
  ) {

      ia[i] =
          byteString.charCodeAt(i);

  }


  var blob =
      new Blob(
          [ab],
          {
              type: mimeString
          }
      );

  return blob;
}


// ===============================
// CAPTURE PHOTO
// ===============================

if (captureButton) {

  captureButton.addEventListener(
      'click',
      event => {

          canvasElement.style.display =
              'block';

          videoPlayer.style.display =
              'none';

          captureButton.style.display =
              'none';


          let context =
              canvasElement.getContext('2d');


          // FIXED: use canvasElement instead of canvas
          let canvasWidth =
              canvasElement.width;


          let canvasHeight =
              videoPlayer.videoHeight /
              (
                  videoPlayer.videoWidth /
                  canvasElement.width
              );


          context.drawImage(
              videoPlayer,
              0,
              0,
              canvasWidth,
              canvasHeight
          );


          if (
              videoPlayer.srcObject
          ) {

              videoPlayer
                  .srcObject
                  .getVideoTracks()
                  .forEach(
                      tracks => tracks.stop()
                  );

          }


          picture =
              canvasElement.toDataURL();


          sendPictureToServer(picture);

      }
  );

}


// ===============================
// SEND PICTURE
// ===============================

const sendPictureToServer = (picture) => {

  var url =
      window.location.href;


  $.ajax({

      type: "POST",

      url: url,

      data: {
          picture: picture
      },

      success: function(data) {

          console.log('data');

      }

  });

};


// ===============================
// OPEN FORM
// ===============================

function openCreatePostModal() {

  if (form) {
      form.style.display = 'block';
  }

  if (captureButton) {
      captureButton.style.display =
          'inline-block';
  }


  // Reset location selection
  if (useGpsCheckbox) {
      useGpsCheckbox.checked = false;
  }

  if (latInput) {
      latInput.value = '';
  }

  if (lngInput) {
      lngInput.value = '';
  }


  updateLocationOption();


  initializeMedia();
}


// ===============================
// CLOSE FORM
// ===============================

function closeCreatePostModal() {

  if (form) {
      form.style.display = 'none';
  }

  if (imagePickerArea) {
      imagePickerArea.style.display = 'none';
  }

  if (videoPlayer) {
      videoPlayer.style.display = 'none';
  }

  if (canvasElement) {
      canvasElement.style.display = 'none';
  }

  if (capture_div) {
      capture_div.style.display = 'none';
  }

  if (upload_section) {
      upload_section.style.display = 'none';
  }

  if (image_options) {
      image_options.style.display = 'flex';
  }

}


// ===============================
// BUTTON EVENTS
// ===============================

if (add_btn) {

  add_btn.addEventListener(
      'click',
      openCreatePostModal
  );

}


if (close_btn) {

  close_btn.addEventListener(
      'click',
      closeCreatePostModal
  );

}


if (capture_btn) {

  capture_btn.addEventListener(
      'click',
      () => {

          if (capture_div) {
              capture_div.style.display =
                  'block';
          }

          if (image_options) {
              image_options.style.display =
                  'none';
          }

      }
  );

}


if (upload_btn) {

  upload_btn.addEventListener(
      'click',
      () => {

          if (upload_section) {
              upload_section.style.display =
                  'block';
          }

          if (image_options) {
              image_options.style.display =
                  'none';
          }

      }
  );

}


// document.addEventListener('DOMContentLoaded', function() {
//     // nav menu
//     const menus = document.querySelectorAll('.side-menu');
//     M.Sidenav.init(menus, {edge: 'right'});
//     // add recipe form
//     // M.Sidenav.init(forms, {edge: 'left'});
//     // forms.addEventListener(click)

//   });


//   const add_btn = document.querySelector('.add-btn');
//   const close_btn = document.querySelector('.close-btn');
//   const form = document.querySelector('.side-form');
//   const capture_div = document.querySelector('.capture-div')
//   const videoPlayer = document.querySelector('#player');
//   const canvasElement = document.querySelector('#canvas');
//   const captureButton = document.querySelector('#capture-btn');
//   const imagePicker = document.querySelector('#image-picker');
//   const imagePickerArea = document.querySelector('#pick-image');


//   const locationBtn = document.querySelector('#location-btn');
//   const locationLoader = document.querySelector('#location-loader');
//   const latInput = document.querySelector('#lat');
//   const lngInput = document.querySelector('#lng');


//   const capture_btn = document.querySelector('.capture-btn');
//   const upload_btn = document.querySelector('.upload-btn');
//   const image_options = document.querySelector('.image-options');
//   const upload_section = document.querySelector('.upload-section');
//   locationBtn.addEventListener('click',()=>{
//     if (!('geolocation' in navigator)) {
//       return;
//     }

//     locationBtn.style.display = 'none';
//     locationLoader.style.display = 'block';
    
//     // capture_div.style.display = 'none';

//     navigator.geolocation.getCurrentPosition(position =>{
//       locationBtn.style.display = 'inline-block';
//       locationLoader.style.display = 'none';

//       fetchedLocation = {lat: position.coords.latitude, lng: position.coords.longitude};
//       latInput.value = `${fetchedLocation.lat.toFixed(4)}`
//       lngInput.value = `${fetchedLocation.lng.toFixed(4)}`
//     },(err) =>{
//       locationBtn.style.display = 'inline-block';
//       locationLoader.style.display = 'none';
  
//     alert('Please allow location access to proceed!');

//       fetchedLocation = {lat: 0, lng: 0};
//     },{timeout:7000})
//   })
  
//    getCamera = async () => {
//     let devices = await navigator.mediaDevices.enumerateDevices()
//     camaras = devices.filter(device => device.kind === 'videoinput')
//     deviceID= camaras[camaras.length -1].deviceId
//     // console.log(deviceID)
//     return deviceID
//   }
//   const initializeMedia = () =>{
    
//     if(!('mediaDevices' in navigator)){   // if mediaDevices not in navigator create ownpolyfill
//       navigator.mediaDevices = {};
//       console.log(navigator)
//     }

//     if(!('getUserMedia' in navigator.mediaDevices)){
//       navigator.mediaDevices.getUserMedia = function(constraints){
//         let getUserMedia = navigator.webkitGetUserMedia || navigator.mozGetUserMedia;    //for  safari or mozilla
//         if(!getUserMedia){
//           return Promise.reject(new Error('getUserMedia is not implemented!'));   // if modern getUserMedia not found
//         }
//         return new Promise((resolve,reject)=>{
//           getUserMedia.call(navigator,constraints,resolve,reject);
//         })
//       }
//     }
//     getCamera().then(cID=>{
//       let streamConstraints={ video: { deviceId: cID } }
//       console.log(streamConstraints)

//       navigator.mediaDevices.getUserMedia(streamConstraints)
//       .then(function(stream){
//         videoPlayer.srcObject = stream;
//         videoPlayer.style.display = 'block';
//       })
//       .catch(function(err){
//         imagePickerArea.style.display = 'block';
//       })
//     })
//   }

//   let picture;
//   function dataURItoBlob(dataURI) {
//     var byteString = atob(dataURI.split(',')[1]);
//     var mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0]
//     var ab = new ArrayBuffer(byteString.length);
//     var ia = new Uint8Array(ab);
//     for (var i = 0; i < byteString.length; i++) {
//       ia[i] = byteString.charCodeAt(i);
//     }
//     var blob = new Blob([ab], {type: mimeString});
//     return blob;
//   }

//   captureButton.addEventListener('click',event =>{
//     canvasElement.style.display = 'block';
//     videoPlayer.style.display = 'none';
//     captureButton.style.display = 'none';

//     let context = canvasElement.getContext('2d');
//     let canvasWidth = canvas.width;
//     let canvasHeight = videoPlayer.videoHeight/(videoPlayer.videoWidth / canvas.width);
//     context.drawImage(videoPlayer,0,0,canvasWidth,canvasHeight); // draw image on canvas
//     videoPlayer.srcObject.getVideoTracks().forEach(tracks => tracks.stop());   //stop video once image is captured

//     // picture = dataURItoBlob(canvasElement.toDataURL());
//     picture = canvasElement.toDataURL();
//     sendPictureToServer(picture);
//   })

//   sendPictureToServer = (picture) =>{
//     var url = window.location.href;
//     $.ajax(
//       {
//           type:"POST",
//           url: url,
//           data:{picture: picture},
//           success: function( data ) 
//           {
//               console.log('data')
//           }
//        })
//   }



  
//   function openCreatePostModal() {
//     form.style.display = 'block';
//     captureButton.style.display = 'inline-block';
//     initializeMedia();
//   }

//   function closeCreatePostModal() {
//     form.style.display = 'none';
//     imagePickerArea.style.display = 'none';
//     videoPlayer.style.display = 'none';
//     canvasElement.style.display = 'none';
//     capture_div.style.display='none';
//     upload_section.style.display="none";

//     image_options.style.display = 'flex';

//   }
  
//   add_btn.addEventListener('click', openCreatePostModal);
//   close_btn.addEventListener('click', closeCreatePostModal);

//   capture_btn.addEventListener('click',()=>{
//     capture_div.style.display='block';
//     image_options.style.display = 'none';
//   })

//   upload_btn.addEventListener('click',()=>{
//     upload_section.style.display="block";
//     image_options.style.display = 'none';

//   })