export default function Home() {
  return (
    <div className="flex flex-col justify-center min-h-screen py-2 bg-purple-600 bg-opacity-25">
      <div className="grid place-items-center grid-cols-2 gap-3">
        <div>
          <form className="w-full max-w-sm">
            <div className="flex items-center border-b border-teal-500 py-2">
              <input className="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" type="text" placeholder="input image link" aria-label="Full name">
              </input>
              <button className="flex-shrink-0 bg-purple-500 hover:bg-purple-700 border-purple-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded" type="button">
                Enter
              </button>
            </div>
          </form>
        </div>
        <div></div>
      </div>

      <main className="flex flex-col items-center justify-center w-full flex-1 px-20 text-center">

      </main>


      <footer className="flex items-center justify-center w-full h-24 border-t bg-purple-100 bg-opacity-50">
        <a
          className="flex items-center justify-center font-mono"
          target="_blank"
          rel="noopener noreferrer"
        >
          Developed by albert wan, sebastian wueste, and damian ramos

        </a>
      </footer>
    </div>
  )
}
