from selene import browser

def test_sending_registration_form(browser_management):
    browser.open('/automation-practice-form')
    browser.element('[id="firstName"]').type('Vladimir')
    browser.element('[id="lastName"]').type('Serov')
    browser.element('[id="userEmail"]').type('hello.serov@gmail.com')
    browser.element('//*[@id="genterWrapper"]/div[2]/div[1]').click()
    browser.element('[id="userNumber"]').type('8800555353')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[value="1996"]').click()
    browser.element('[value="0"]').click()
    browser.element('[aria-label="Choose Friday, January 5th, 1996"]').click()
    browser.element('[id="subjectsInput"]').type('Computer').press_enter()


