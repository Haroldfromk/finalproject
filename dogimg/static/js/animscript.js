(() => {
    // DOM을 통해 요소들을 저장합니다
    const viewer = document.querySelector('#cat_ani .cont_viewer');
    const viewerWidth = viewer.offsetWidth/2;
    const bgNear = document.querySelector('#cat_ani .bg_forest_near');
    const bgFar = document.querySelector('#cat_ani .bg_forest_far');
    const objCat = document.querySelector('#cat_ani .obj_cat');
    const objFriend1 = document.querySelector('#cat_ani .obj_friend1');
    const objFriend2 = document.querySelector('#cat_ani .obj_friend2');
    const objFriend3 = document.querySelector('#cat_ani .obj_friend3');
    const objFriend1_pos = objFriend1.offsetLeft-viewerWidth;
    const objFriend2_pos = objFriend2.offsetLeft-viewerWidth;
    const objFriend3_pos = objFriend3.offsetLeft-viewerWidth;

    // 배경의 이동 속도를 제어합니다
    let speed = 3;
    let moveNear = 0;
    let moveFar = 0;

    // 가까운 배경과 먼 배경의 속도에 차이를 두어 원근감을 줍니다
    let speedNear = speed + 5;
    let speedFar = speed + 1;

    // 냥이에게 걷는 애니메이션이 들어간 클래스를 부여합니다
    const funcSkinChanger = () => {
        objCat.classList.add('img_walk');
    }

    // 냥이에게 걷는 애니메이션이 들어간 클래스를 제거합니다
    const funcSkinRecover = () => {
        objCat.classList.remove('img_walk');
    }

    // 방향키에 따라 냥이의 몸을 회전시킵니다
    const funcDirection = (arrow) => {
        if (arrow === 'front') {
            objCat.style.transform = 'rotateY(0)';
        } else {
            objCat.style.transform = 'rotateY(180deg)';
        }
    }

    // 오른쪽으로 이동할 때의 동작들을 수행하는 함수입니다. 배경을 왼쪽으로 움직여 냥이가 걷는것 처럼 보이게 합니다.
    const funcBgMoveRight = (near, far) => {
        moveNear = moveNear - speedNear;
        moveFar = moveFar - speedFar;
        near.style.transform = `translateX(${moveNear}px)`;
        far.style.transform = `translateX(${moveFar}px)`;
        funcSkinChanger();
        funcDirection('front');
    }

    // 왼쪽으로 이동할때의 동작들을 수행하는 함수입니다. 배경을 오른쪽으로 움직여 냥이가 뒤로가는것 처럼 보이게 합니다.
    const funcBgMoveLeft = (near, far) => {
        moveNear = moveNear + speedNear;
        moveFar = moveFar + speedFar;
        near.style.transform = `translateX(${moveNear}px)`;
        far.style.transform = `translateX(${moveFar}px)`;
        funcSkinChanger();
        funcDirection('back');
    }

    // 방향키에 따른 동작을 수행하는 함수입니다
    const funcBgMove = (e) => {
        switch (e.keyCode) {
            case 39: // 우로 이동
                if(-(bgNear.style.transform.slice(11, -3))>objFriend1_pos){
                    objFriend1.classList.add('obj_contect');
                }
                if(-(bgNear.style.transform.slice(11, -3))>objFriend2_pos){
                    objFriend2.classList.add('obj_contect');
                }
                if(-(bgNear.style.transform.slice(11, -3))>objFriend3_pos){
                    objFriend3.classList.add('obj_contect');
                }
                if(-(bgNear.style.transform.slice(11, -3)) <= bgNear.offsetWidth){//배경의 넓이보다 더 이동하면 이동 불가
                    funcBgMoveRight(bgNear, bgFar);
                }
                break;

            case 37: // 좌로 이동
                if ((bgNear.style.transform).slice(11, -3) <= 0) { //배경의 좌표가 0보다 작으면 이동 불가
                    funcBgMoveLeft(bgNear, bgFar);
                }
                break;
        }
    }

    // 키를 눌렀을 때를 감지합니다
    window.addEventListener('keydown', (e) => {
        return funcBgMove(e);
    });

    // 키를 때었을 때를 감지합니다. 걷기 애니메이션을 제거합니다.
    window.addEventListener('keyup', () => {
        return funcSkinRecover();
    });
})();