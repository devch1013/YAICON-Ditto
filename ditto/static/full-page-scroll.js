	  const TIME_OUT = 1200 // It should be the same transition time of the sections
      const body = document.querySelector('body')
      const layout = document.querySelector('.layout')
      const sectionsQty = document.querySelectorAll('section').length
      const sectionStick = document.querySelector('.section-stick')

      let startFlag = true
      let initialScroll = window.scrollY
      let qty = 1,
        main = null,
        next = null

      let end, footer

      // Add child elements in .section-stick as number of sections exist
      Array(sectionsQty)
        .fill()
        .forEach(() => {
          sectionStick.innerHTML = sectionStick.innerHTML + '<div class="stick"></div>'
        })

      console.log('SLIDE', qty)

      // Listening to scroll event
      window.onscroll = () => {
        if (startFlag) {
          const scrollDown = this.scrollY >= initialScroll
          // TODO: crear una constante para sectionsQty + 1
          const scrollLimit = qty >= 1 && qty <= sectionsQty + 1

          // Verify that the scroll does not exceed the number of sections
          if (scrollLimit) {
            body.style.overflowY = 'hidden' // Lock el scroll

            if (scrollDown && qty < sectionsQty) {
              main = document.querySelector(`section.s${qty}`)
              next = document.querySelector(`section.s${qty + 1}`)

              main.style.top = '-100vh'
              next.style.top = '0'

              qty++
            } else if (!scrollDown && qty > 1) {
              if (qty !== sectionsQty + 1) {
                main = document.querySelector(`section.s${qty - 1}`)
                next = document.querySelector(`section.s${qty}`)

                main.style.top = '0'
                next.style.top = '100vh'
              } else body.classList.remove('end')

              qty--
            } else {
              // Mark the end of the slider on the body
              body.classList.add('end')
              qty++
            }

            // Scroll progressbar
            if (qty !== sectionsQty + 1) {
              const active = document.querySelector('.section-stick .stick.active')
              active.style.top = (62 + 30) * (qty - 1) + 'px'
            }
          }

          console.log('SLIDE', qty)

          // Wait for the scrolling to finish to reset the values
          setTimeout(() => {
            initialScroll = this.scrollY
            startFlag = true
            body.style.overflowY = 'scroll' // Unlock scroll
          }, TIME_OUT)

          startFlag = false
        }

        // Keep scrollbar in the middle of the viewport
        window.scroll(0, window.screen.height)
      }