from selene import browser, have, be
import os

# Filling the form
def test_sending_registration_form(browser_management):
    browser.open('/automation-practice-form')
    browser.element('[id="firstName"]').type('Vladimir')
    browser.element('[id="lastName"]').type('Serov')
    browser.element('[id="userEmail"]').type('hello@gmail.com')
    browser.element('//*[@id="genterWrapper"]/div[2]/div[1]').click()
    browser.element('[id="userNumber"]').type('8800555353')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[value="1996"]').click()
    browser.element('[value="0"]').click()
    browser.element('[aria-label="Choose Friday, January 5th, 1996"]').click()
    browser.element('[id="subjectsInput"]').type('Computer').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    input_field = browser.element('#uploadPicture')
    input_field.send_keys(os.getcwd() + '\img\Mona_Lisa1.jpg')
    browser.element('#currentAddress').type('Novgorod')
    browser.element('#state').click()
    browser.all("#state div").element_by(have.exact_text("NCR")).click()
    browser.element('#city').click()
    browser.all("#city div").element_by(have.exact_text("Delhi")).click()
    browser.element('#submit').click()

    #Testing modal window data
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.modal-body').should(have.text('Vladimir Serov'))
    browser.element('.modal-body').should(have.text('hello@gmail.com'))
    browser.element('.modal-body').should(have.text('Male'))
    browser.element('.modal-body').should(have.text('8800555353'))
    browser.element('.modal-body').should(have.text('05 January,1996'))
    browser.element('.modal-body').should(have.text('Computer Science'))
    browser.element('.modal-body').should(have.text('Sports'))
    browser.element('.modal-body').should(have.text('Mona_Lisa1.jpg'))
    browser.element('.modal-body').should(have.text('Novgorod'))
    browser.element('.modal-body').should(have.text('NCR Delhi'))

